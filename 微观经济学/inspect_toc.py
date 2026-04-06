import fitz

def print_toc(filepath):
    doc = fitz.open(filepath)
    toc = doc.get_toc()
    for t in toc:
        print(t)
        
    print(f"Total Pages: {len(doc)}")

if __name__ == "__main__":
    print_toc(r"E:\workspace\ddl\微观经济学\微观经济学-现代观点-范里安-练习册答案+英文版.pdf")
