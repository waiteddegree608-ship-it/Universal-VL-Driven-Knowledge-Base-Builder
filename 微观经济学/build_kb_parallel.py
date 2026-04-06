import os
import re
import fitz
import win32com.client
import base64
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from openai import OpenAI

# Configuration
import random

# Configuration
API_KEYS = [
    "sk-glinbzmkuqfkveeqeiizatpkwseliggmflxybeqtmxrmcwhz",
    "sk-zgvbclgybcdulimggbvomgrsiwcatbrnabdjmoeqtpqtpovp",
    "sk-vxrxkhmyddrepezetcpzxqlpxxljtsyqapbzuxwzqbjtfani",
    "sk-gtfjrsimjzwqchlgbqnqhyfhmvpjsepmhmoyuzofjckjwxma",
    "sk-qlwvlwfhsmchubyvgsrrmfebvlhsdkuguxvaybdgjzjkxjjv",
    "sk-frecyckaruoozoevilwsxxhhotyklwwhcriykjqosdnkykun"
]
BASE_URL = "https://api.siliconflow.cn/v1"
MODEL_NAME = "Qwen/Qwen3-VL-235B-A22B-Thinking"

BASE_DIR = r"E:\workspace\ddl\微观经济学"
TEMP_DIR = os.path.join(BASE_DIR, "temp_assets")
OUTPUT_DIR = os.path.join(BASE_DIR, "kb_output")
PDF_PATH = os.path.join(BASE_DIR, "微观经济学-现代观点-范里安-练习册答案+英文版.pdf")
PPT_DIR = os.path.join(BASE_DIR, "ppt")

if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def get_client():
    # Randomly select a key for load balancing
    key = random.choice(API_KEYS)
    return OpenAI(api_key=key, base_url=BASE_URL)

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def call_vl_api(image_path, context=""):
    base64_image = encode_image(image_path)
    prompt = f"Context: {context}\nPlease analyze this page/slide in detail. Extract all text, formulas, and explain any charts/graphs. Return in Markdown."
    
    retries = 5
    backoff = 2
    
    # Get a fresh client (and key) for this attempt sequence
    # Or maybe rotate per retry? Let's rotate per attempt to failover fast.
    
    for attempt in range(retries):
        try:
            current_client = get_client()
            response = current_client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}},
                        ],
                    }
                ],
                max_tokens=4096
            )
            return response.choices[0].message.content
        except Exception as e:
            error_str = str(e)
            if "429" in error_str:
                 wait_time = backoff * (2 ** attempt)
                 log(f"Rate Limited (429) on {os.path.basename(image_path)}. Retrying in {wait_time}s...")
                 time.sleep(wait_time)
            else:
                 log(f"Error processing {os.path.basename(image_path)} (Attempt {attempt+1}): {e}")
                 time.sleep(5)
    return f"[Failed to process {os.path.basename(image_path)}]"

# --- Step 1: Asset Extraction ---

def get_pdf_structure(filepath):
    doc = fitz.open(filepath)
    chapters = {}
    quizzes = {}
    
    # 1. Scan for markers
    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text("text")
        lines = text.split('\n')
        for line in lines[:15]:
            line = line.strip().lower()
            if not line: continue
            
            # Match "Chapter N"
            if line.startswith("chapter"):
                parts = line.split()
                if len(parts) >= 2 and parts[1].isdigit():
                    num = int(parts[1])
                    if num not in chapters:
                        chapters[num] = i + 1
            
            # Match "Quiz N"
            if line.startswith("quiz"):
                 parts = line.split()
                 if len(parts) >= 2 and parts[1].isdigit():
                     num = int(parts[1])
                     if num not in quizzes:
                         quizzes[num] = i + 1

    # 2. Add last boundaries
    total_pages = len(doc)
    
    # Fill in Quiz 1 if missing (Assume usually after last chapter or check known location)
    # Based on user info: Last Chapter is 36. 
    # Current heuristic: Quizzes start around 440.
    if 1 not in quizzes and 2 in quizzes:
        # Heuristic: Quiz 1 starts after Ch 36 ends? Or somewhere before Quiz 2
        # Let's assume Quiz 1 is at start of Quiz Section if not found?
        # Actually, let's just proceed with what we found.
        pass

    return chapters, quizzes, total_pages

def extract_pdf_images(chapters, quizzes, total_pages):
    log("Extracting PDF images...")
    doc = fitz.open(PDF_PATH)
    pdf_assets = {} # { 'Chapter_1': [path1, path2], 'Quiz_1': ... }
    
    # Process Chapters
    sorted_ch = sorted(chapters.items())
    for idx, (ch_num, start_page) in enumerate(sorted_ch):
        # End page is start of next Chapter or start of first Quiz (if this is last chapter)
        if idx < len(sorted_ch) - 1:
            end_page = sorted_ch[idx+1][1] - 1
        else:
            # Last chapter ends where first quiz starts (roughly)
            # Find the minimum quiz page
            if quizzes:
                first_quiz_page = min(quizzes.values())
                end_page = first_quiz_page - 1
            else:
                end_page = total_pages # Fallback
        
        # Extract pages
        assets = []
        page_dir = os.path.join(TEMP_DIR, f"pdf_ch_{ch_num}")
        if not os.path.exists(page_dir):
            os.makedirs(page_dir)
            
        for p in range(start_page - 1, end_page): # fitz is 0-indexed
            if p >= total_pages: break
            pix = doc[p].get_pixmap(matrix=fitz.Matrix(2, 2))
            path = os.path.join(page_dir, f"page_{p+1}.png")
            pix.save(path)
            assets.append(path)
        
        pdf_assets[f"Chapter_{ch_num}"] = assets

    # Process Quizzes
    sorted_q = sorted(quizzes.items())
    for idx, (q_num, start_page) in enumerate(sorted_q):
        if idx < len(sorted_q) - 1:
            end_page = sorted_q[idx+1][1] - 1
        else:
            end_page = total_pages
            
        assets = []
        page_dir = os.path.join(TEMP_DIR, f"pdf_quiz_{q_num}")
        if not os.path.exists(page_dir): os.makedirs(page_dir)
        
        for p in range(start_page - 1, end_page):
            if p >= total_pages: break
            pix = doc[p].get_pixmap(matrix=fitz.Matrix(2, 2))
            path = os.path.join(page_dir, f"page_{p+1}.png")
            pix.save(path)
            assets.append(path)
            
        pdf_assets[f"Quiz_{q_num}"] = assets
        
    return pdf_assets

def extract_ppt_images():
    log("Extracting PPT images...")
    ppt_assets = {} # { 'Ch01.ppt': [path1, ...] }
    
    files = [f for f in os.listdir(PPT_DIR) if f.endswith(('.ppt', '.pptx'))]
    if not files: return {}
    
    try:
        powerpoint = win32com.client.Dispatch("PowerPoint.Application")
        # powerpoint.Visible = 1
        
        for f in files:
            abs_path = os.path.join(PPT_DIR, f)
            ppt_name = os.path.splitext(f)[0]
            out_dir = os.path.join(TEMP_DIR, f"ppt_{ppt_name}")
            if not os.path.exists(out_dir): os.makedirs(out_dir)
            
            assets = []
            
            # Open & Export
            try:
                prs = powerpoint.Presentations.Open(abs_path, WithWindow=False)
                for i, slide in enumerate(prs.Slides):
                    img_path = os.path.join(out_dir, f"slide_{i+1}.png")
                    # Check if exists to skip (resuming)
                    if not os.path.exists(img_path):
                        slide.Export(img_path, "PNG")
                    assets.append(img_path)
                prs.Close()
                ppt_assets[ppt_name] = assets
            except Exception as e:
                log(f"Failed to export {f}: {e}")
                
        # powerpoint.Quit()
    except Exception as e:
        log(f"PPT Error: {e}")
        
    return ppt_assets

# --- Step 2: Parallel Processing ---

def process_task(task_name, image_paths):
    log(f"Task started: {task_name} ({len(image_paths)} images)")
    details = []
    for img in image_paths:
        content = call_vl_api(img, context=task_name)
        details.append(content)
        # Minimal sleep just to be safe, but keys should handle it
        # time.sleep(0.5) 
    
    full_text = f"## {task_name}\n\n" + "\n\n---\n\n".join(details)
    
    # Write immediate result to file
    out_path = os.path.join(OUTPUT_DIR, f"{task_name}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_text)
        
    log(f"Task finished: {task_name}")
    return task_name

def main():
    # 1. Preprocess / Asset Generation
    chapters, quiz_starts, total_pages = get_pdf_structure(PDF_PATH)
    pdf_tasks = extract_pdf_images(chapters, quiz_starts, total_pages)
    ppt_tasks = extract_ppt_images()
    
    # 2. Execution Queue
    # We have 6 keys. Parallelism 12 means ~2 threads per key. Should be safe.
    with ThreadPoolExecutor(max_workers=12) as executor: 
        futures = []
        
        # PDF Chapter & Quiz Tasks
        # We can group them: Task "Unit_N" = Chapter_N + Quiz_N
        # Or just run all separate keys
        # User said "Group corresponding Chapter and Quiz"
        
        # Let's map chapters and quizzes
        
        # Prepare valid Task Units
        # Keys in pdf_tasks are "Chapter_N" or "Quiz_N"
        
        # Merge dicts
        all_work_items = {} 
        
        # PDF items
        for key, assets in pdf_tasks.items(): 
            if not assets: continue
            # key is like "Chapter_1"
            all_work_items[f"PDF_{key}"] = assets
            
        # PPT items
        for key, assets in ppt_tasks.items():
            if not assets: continue
            all_work_items[f"PPT_{key}"] = assets
            
        log(f"Starting {len(all_work_items)} tasks in parallel...")
        
        for name, assets in all_work_items.items():
            futures.append(executor.submit(process_task, name, assets))
            
        for future in as_completed(futures):
            try:
                res = future.result()
            except Exception as e:
                log(f"Task crashed: {e}")

    # 3. Final Merge
    log("Merging Knowledge Base...")
    final_kb = "# 微观经济学 全面知识库\n\n"
    
    # Order sensibly
    # Chapters 1..36, pairing with PPT and Quiz matches?
    # Simple sort by filename in output dir
    
    md_files = sorted([f for f in os.listdir(OUTPUT_DIR) if f.endswith(".md")])
    for md in md_files:
        with open(os.path.join(OUTPUT_DIR, md), "r", encoding="utf-8") as f:
            final_kb += f.read() + "\n\n"
            
    with open(os.path.join(BASE_DIR, "knowledge_base_final.md"), "w", encoding="utf-8") as f:
        f.write(final_kb)
        
    log("All Done!")

if __name__ == "__main__":
    main()
