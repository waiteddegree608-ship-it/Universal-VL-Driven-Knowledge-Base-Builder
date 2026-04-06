import os
import random
import time
import base64
import fitz  # PyMuPDF
import win32com.client
from concurrent.futures import ThreadPoolExecutor, as_completed
from openai import OpenAI

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

if not os.path.exists(TEMP_DIR): os.makedirs(TEMP_DIR)
if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def call_vl_api_iterative(client, image_path, previous_context):
    base64_image = encode_image(image_path)
    
    # Prompt: Analyze current image, given previous context
    prompt = "你是微观经济学专家。请基于【上文知识点总结】，对【当前图片】进行详细解析。\n" \
             "1. 提取当前图片中的所有文字、公式。\n" \
             "2. 如果有图表，结合上文详细解释其变化的含义。\n" \
             "3. 输出为Markdown格式，不要重复上文中已有的废话，但要保持知识的连续性。\n\n" \
             f"【上文知识点总结】: {previous_context[-2000:]}...\n" # Limit context size
             
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}},
            ],
        }
    ]

    retries = 10
    backoff = 2
    
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                max_tokens=4096
            )
            return response.choices[0].message.content
        except Exception as e:
            wait_time = backoff * (1.5 ** attempt)
            log(f"Error on {os.path.basename(image_path)}: {e}. Retry in {int(wait_time)}s...")
            time.sleep(wait_time)
            
    raise Exception(f"Failed to process {image_path} after {retries} attempts")

def process_folder_task(api_key_ignored, task_name, image_paths):
    """
    Process a single folder (Chapter/PPT) sequentially.
    Picks a RANDOM key for each request to spread load across all 6 keys.
    """
    
    log(f"Started task: {task_name}")
    
    accumulated_knowledge = ""
    page_results = []
    
    for idx, img_path in enumerate(image_paths):
        log(f"[{task_name}] Processing image {idx+1}/{len(image_paths)}...")
        
        try:
            # Randomly select a key for EACH request
            current_key = random.choice(API_KEYS)
            client = OpenAI(api_key=current_key, base_url=BASE_URL)
            
            # Pass accumulated knowledge
            context = accumulated_knowledge
            
            result = call_vl_api_iterative(client, img_path, context)
            
            page_results.append(f"### Page/Slide {idx+1}\n\n{result}\n")
            accumulated_knowledge += result + "\n"
            
            # Tiny sleep to be nice
            time.sleep(1)
            
        except Exception as e:
            log(f"[{task_name}] CRITICAL FAILURE on image {idx+1}: {e}")
            return False 
            
    # Save final result
    out_path = os.path.join(OUTPUT_DIR, f"{task_name}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# {task_name}\n\n" + "\n---\n".join(page_results))
        
    log(f"Finished task: {task_name}")
    return True

# --- Asset Extraction (Same as before) ---
def get_pdf_structure(filepath):
    doc = fitz.open(filepath)
    chapters, quizzes = {}, {}
    for i in range(len(doc)):
        text = doc[i].get_text("text").split('\n')
        for line in text[:15]:
            line = line.strip().lower()
            if not line: continue
            if line.startswith("chapter"):
                parts = line.split()
                if len(parts) >= 2 and parts[1].isdigit():
                    num = int(parts[1])
                    if num not in chapters: chapters[num] = i + 1
            if line.startswith("quiz"):
                 parts = line.split()
                 if len(parts) >= 2 and parts[1].isdigit():
                     num = int(parts[1])
                     if num not in quizzes: quizzes[num] = i + 1
    
    # Fill gaps safely
    # Manual Fix for Quiz 1 if missing (Based on observation "Page 440: QUIZZES")
    if 1 not in quizzes:
        quizzes[1] = 440
        
    return chapters, quizzes, len(doc)

def extract_pdf_images(chapters, quizzes, total_pages):
    doc = fitz.open(PDF_PATH)
    tasks = {}
    
    # Helper to extract range
    def extract_range(name, start, end):
        p_dir = os.path.join(TEMP_DIR, name)
        if not os.path.exists(p_dir): os.makedirs(p_dir)
        assets = []
        for p in range(start-1, end):
            if p >= total_pages: break
            path = os.path.join(p_dir, f"page_{p+1}.png")
            if not os.path.exists(path):
                doc[p].get_pixmap(matrix=fitz.Matrix(2,2)).save(path)
            assets.append(path)
        return assets

    # Chapters
    sorted_ch = sorted(chapters.items())
    for i, (num, start) in enumerate(sorted_ch):
        end = sorted_ch[i+1][1]-1 if i < len(sorted_ch)-1 else (min(quizzes.values())-1 if quizzes else total_pages)
        tasks[f"PDF_Chapter_{num}"] = extract_range(f"pdf_ch_{num}", start, end)

    # Quizzes
    sorted_q = sorted(quizzes.items())
    for i, (num, start) in enumerate(sorted_q):
        end = sorted_q[i+1][1]-1 if i < len(sorted_q)-1 else total_pages
        tasks[f"PDF_Quiz_{num}"] = extract_range(f"pdf_quiz_{num}", start, end)
        
    return tasks

def extract_ppt_images():
    tasks = {}
    files = [f for f in os.listdir(PPT_DIR) if f.endswith(('.ppt', '.pptx'))]
    if not files: return {}
    
    try:
        # ppt_app = win32com.client.Dispatch("PowerPoint.Application")
        # Ensure single threaded apartment
        import pythoncom
        pythoncom.CoInitialize()
        ppt_app = win32com.client.Dispatch("PowerPoint.Application")
        
        for f in files:
            name = os.path.splitext(f)[0]
            out_dir = os.path.join(TEMP_DIR, f"ppt_{name}")
            if not os.path.exists(out_dir): os.makedirs(out_dir)
            
            assets = []
            try:
                prs = ppt_app.Presentations.Open(os.path.join(PPT_DIR, f), WithWindow=False)
                for i, slide in enumerate(prs.Slides):
                    path = os.path.join(out_dir, f"slide_{i+1}.png")
                    if not os.path.exists(path): slide.Export(path, "PNG")
                    assets.append(path)
                prs.Close()
                tasks[f"PPT_{name}"] = assets
            except Exception as e:
                log(f"Error exporting PPT {f}: {e}")
    except Exception as e:
        log(f"PPT App Error: {e}")
    
    return tasks

def main():
    log("Scanning assets...")
    ch, q, total = get_pdf_structure(PDF_PATH)
    pdf_tasks = extract_pdf_images(ch, q, total)
    ppt_tasks = extract_ppt_images()
    
    all_tasks = {**pdf_tasks, **ppt_tasks}
    task_keys = list(all_tasks.keys())
    # Sort to enable resuming or logical order (optional)
    task_keys.sort() 
    
    # Filter out already completed tasks AND exclude PPTs for now as requested
    todo_keys = [k for k in task_keys if not os.path.exists(os.path.join(OUTPUT_DIR, f"{k}.md")) and not k.startswith("PPT")]
    
    # Custom Sort: PDF Chapters First -> PDF Quizzes -> PPT
    # And sort numerically: Chapter_2 before Chapter_10
    def sort_key(key):
        # Priority: PDF_Chapter = 0, PDF_Quiz = 1, PPT = 2
        prio = 3
        if key.startswith("PDF_Chapter"): prio = 0
        elif key.startswith("PDF_Quiz"): prio = 1
        elif key.startswith("PPT"): prio = 2
        
        # Extract number
        import re
        nums = re.findall(r'\d+', key)
        num = int(nums[0]) if nums else 999
        
        return (prio, num)
        
    todo_keys.sort(key=sort_key)
    
    log(f"Total tasks: {len(task_keys)}. Remaining: {len(todo_keys)}")
    log(f"Top 5 tasks: {todo_keys[:5]}")
    
    # Queue-based Worker Model
    import queue
    task_queue = queue.Queue()
    for t in todo_keys:
        task_queue.put(t)
        
    def worker_loop(worker_id):
        log(f"Worker {worker_id} started.")
        while not task_queue.empty():
            try:
                task_name = task_queue.get_nowait()
            except queue.Empty:
                break
                
            log(f"Worker {worker_id} picked up {task_name}")
            try:
                # Pass None for api_key as it is now random inside
                success = process_folder_task(None, task_name, all_tasks[task_name])
                if not success:
                    log(f"Worker {worker_id} failed on {task_name}. Re-queueing?")
            except Exception as e:
                log(f"Worker {worker_id} crashed handling {task_name}: {e}")
                
            task_queue.task_done()
            log(f"Worker {worker_id} finished {task_name}. Checking next...")
            
    # RESTORE PARALLEL EXECUTION (Efficiency Mode)
    # We use N workers. Inside each task, keys are picked randomly per request.
    num_workers = len(API_KEYS)
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = []
        for i in range(num_workers):
            futures.append(executor.submit(worker_loop, i))
            
        for f in as_completed(futures):
            try:
                f.result()
            except Exception as e:
                log(f"A worker thread crashed: {e}")

    # Final Merge
    log("Merging all KBs...")
    final_content = "# Knowledge Base\n\n"
    for k in task_keys:
        p = os.path.join(OUTPUT_DIR, f"{k}.md")
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                final_content += f.read() + "\n\n"
    
    with open(os.path.join(BASE_DIR, "knowledge_base_iterative.py.md"), "w", encoding="utf-8") as f:
        f.write(final_content)
        
    log("Done.")

if __name__ == "__main__":
    main()
