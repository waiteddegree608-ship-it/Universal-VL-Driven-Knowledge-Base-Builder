import os
import time
import base64
import fitz  # PyMuPDF
import win32com.client
from openai import OpenAI
from io import BytesIO

# Configuration
API_KEY = "sk-glinbzmkuqfkveeqeiizatpkwseliggmflxybeqtmxrmcwhz"
BASE_URL = "https://api.siliconflow.cn/v1"
# Priority: User suggested model, then fallback to Qwen2-VL-72B
MODEL_NAME = "Qwen/Qwen2-VL-72B-Instruct" # Fallback/Standard
# Note: If the user explicitly wants 'Qwen/Qwen3-VL-235B-A22B-Thinking' and it exists, we can swap. 
# SiliconFlow documentation usually lists 'Qwen/Qwen2-VL-72B-Instruct'. 
# I will use a reliable High-Res VL model available on SiliconFlow. 
# If the user is sure about the ID, they can edit it, but I'll stick to a known working high-end one to avoid 404s 
# unless I can confirm the other exists. 
# *Correction*: I will prioritize the User's suggestion if it works, but I'll default to the one I know works to avoid crash, 
# or makes it easy to switch. I'll use the user's string in the call if passed.

TARGET_MODEL = "Qwen/Qwen3-VL-235B-A22B-Thinking" 
# User asked for: "Qwen/Qwen3-VL-235B-A22B-Thinking". 
# I will try to use a function that allows fallback? No, let's just use 72B-VL which is powerful enough 
# and definitely exists. If the user insists on the other, they can change it or I can try it.
# Actually, the user's prompt implies they *want* me to use it if I can.
# Let's trust the user's model ID? Or maybe the user is hallucinating the ID?
# "Qwen3" is not widely released as of my last knowledge. 
# I will use Qwen2-VL-72B-Instruct as it is the current SOTA open weight VL on SiliconFlow.
# I will add a comment explaining this.

OUTPUT_FILE = r"E:\workspace\ddl\微观经济学\knowledge_base_vl.md"
TEMP_IMG_DIR = r"E:\workspace\ddl\微观经济学\temp_images"

if not os.path.exists(TEMP_IMG_DIR):
    os.makedirs(TEMP_IMG_DIR)

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def call_vl_api(image_path, context_text=""):
    base64_image = encode_image(image_path)
    
    prompt = "你是一位微观经济学专家。请详细分析这张图片（幻灯片或文档页面）。\n" \
             "1. 如果有图表（如供需曲线、无差异曲线等），请详细解释其含义、坐标轴、曲线移动的原因和结果。\n" \
             "2. 提取页面中的所有文字内容和公式，并进行逻辑整理。\n" \
             "3. 不要遗漏任何细节，将内容整理为Markdown格式。\n" \
             "4. 忽略页眉页脚的无关信息。"
             
    if context_text:
        prompt += f"\n参考文本上下文: {context_text[:500]}..."

    try:
        response = client.chat.completions.create(
            model=TARGET_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=4096 
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"API Error processing {os.path.basename(image_path)}: {e}")
        return f"[Error processing image: {e}]"

def process_pdf(filepath):
    print(f"I will process PDF: {filepath}")
    results = []
    try:
        doc = fitz.open(filepath)
        total_pages = len(doc)
        print(f"Total pages: {total_pages}")
        
        for i, page in enumerate(doc):
            # Render page to image
            zoom = 2  # Higher zoom for better resolution
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            
            img_filename = f"{os.path.basename(filepath)}_page_{i+1}.png"
            img_path = os.path.join(TEMP_IMG_DIR, img_filename)
            pix.save(img_path)
            
            print(f"Processing Page {i+1}/{total_pages}...")
            content = call_vl_api(img_path)
            results.append(f"### Page {i+1}\n\n{content}\n")
            
            # Optional: Sleep to avoid rate limits
            # time.sleep(1)
            
    except Exception as e:
        print(f"Error processing PDF {filepath}: {e}")
    return "\n".join(results)

def process_ppt(filepath):
    print(f"Processing PPT: {filepath}")
    results = []
    try:
        powerpoint = win32com.client.Dispatch("PowerPoint.Application")
        # powerpoint.Visible = 1
        try:
            presentation = powerpoint.Presentations.Open(filepath, WithWindow=False)
        except Exception as e:
            print(f"Failed to open PPT {filepath}: {e}")
            return ""

        total_slides = presentation.Slides.Count
        print(f"Total slides: {total_slides}")
        
        for i, slide in enumerate(presentation.Slides):
            img_filename = f"{os.path.basename(filepath)}_slide_{i+1}.png"
            img_path = os.path.join(TEMP_IMG_DIR, img_filename)
            
            # Export slide
            # PptExportFormat.ppSaveAsPNG = 18 (usually) or just string path with extension
            slide.Export(img_path, "PNG")
            
            print(f"Processing Slide {i+1}/{total_slides}...")
            content = call_vl_api(img_path)
            results.append(f"### Slide {i+1}\n\n{content}\n")
            
        presentation.Close()
    except Exception as e:
        print(f"Error processing PPT {filepath}: {e}")
    return "\n".join(results)

def main():
    base_dir = r"E:\workspace\ddl\微观经济学"
    ppt_dir = os.path.join(base_dir, "ppt")
    pdf_file = os.path.join(base_dir, "微观经济学-现代观点-范里安-练习册答案+英文版.pdf")
    
    # Initialize MD file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# 微观经济学详细知识库 (基于Visual Model解析)\n\n")

    # 1. Process PDF (Optionally specific chapters if too large, but user said 'all')
    if os.path.exists(pdf_file):
        print(f"--- Starting PDF: {os.path.basename(pdf_file)} ---")
        kb_content = process_pdf(pdf_file)
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(f"## {os.path.basename(pdf_file)}\n\n{kb_content}\n---\n\n")

    # 2. Process PPTs
    if os.path.exists(ppt_dir):
        files = sorted(os.listdir(ppt_dir))
        for f in files:
            if f.endswith(('.ppt', '.pptx')):
                path = os.path.join(ppt_dir, f)
                print(f"--- Starting PPT: {f} ---")
                kb_content = process_ppt(path)
                with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                    f.write(f"## {f}\n\n{kb_content}\n---\n\n")

    print("Knowledge Extraction Complete!")

if __name__ == "__main__":
    main()
