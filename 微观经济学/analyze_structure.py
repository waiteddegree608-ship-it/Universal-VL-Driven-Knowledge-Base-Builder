import fitz
import re

def analyze_structure(filepath):
    doc = fitz.open(filepath)
    structure = []
    
    # regex for "Chapter X" or "NAME" which might indicate start
    # The user mentioned "Chapter" and "Quiz".
    # Let's look for "Chapter" at the beginning of text blocks.
    
    chapter_pattern = re.compile(r"^\s*(\d+)\.\s*[A-Za-z]+") # e.g. "1. The Market"
    # Or maybe just "Chapter 1"
    
    print("Scanning pages for Chapters...")
    found_chapters = {}
    found_quizzes = {}
    
    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text("text")
        lines = text.split('\n')
        
        # Heuristic: Check for "Chapter X" or just "X. Title" in first few lines
        # Given the previous output, "Page 393: Chapter 32", likely explicit "Chapter X"
        
        for line in lines[:10]: # Check first 10 lines
            line = line.strip()
            if not line: continue
            
            # Match "Chapter 1", "Chapter 2", ...
            # Be careful of "Chapter 11" appearing in text
            if line.lower().startswith("chapter"):
                parts = line.split()
                if len(parts) >= 2 and parts[1].isdigit():
                    num = int(parts[1])
                    if num not in found_chapters:
                        found_chapters[num] = i + 1
                        print(f"Found Chapter {num} at Page {i+1}")
            
            # Match "Quiz 1", "Quiz 2"
            if line.lower().startswith("quiz"):
                 parts = line.split()
                 if len(parts) >= 2 and parts[1].isdigit():
                     num = int(parts[1])
                     if num not in found_quizzes:
                         found_quizzes[num] = i + 1
                         print(f"Found Quiz {num} at Page {i+1}")

    # Check gaps
    print("\n--- Summary ---")
    sorted_chapters = sorted(found_chapters.items())
    sorted_quizzes = sorted(found_quizzes.items())
    print(f"Chapters found: {len(sorted_chapters)}")
    print(f"Quizzes found: {len(sorted_quizzes)}")

if __name__ == "__main__":
    analyze_structure(r"E:\workspace\ddl\微观经济学\微观经济学-现代观点-范里安-练习册答案+英文版.pdf")
