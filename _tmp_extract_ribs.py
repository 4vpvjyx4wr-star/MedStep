from pypdf import PdfReader

src = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Essential OMM\Block 2\Essential OMM - Ribs and Thoracic Cage.pdf"
dst = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Big lift\MedStep\_tmp_ribs_extract.txt"

reader = PdfReader(src)
parts = []
for i, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    text = text.replace("\x00", "")
    parts.append(f"\n\n===== PAGE {i + 1} =====\n")
    parts.append(text)

text = "".join(parts)
with open(dst, "w", encoding="utf-8") as f:
    f.write(text)
print("chars", len(text))
print("pages", len(reader.pages))
