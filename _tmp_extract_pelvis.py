# Temporary extract script. Delete after the quiz is built.
from pypdf import PdfReader

path = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Essential OMM\Block 3\Essential OMM - Pelvis.pdf"
out = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Big lift\MedStep\_tmp_pelvis_extract.txt"
reader = PdfReader(path)
with open(out, "w", encoding="utf-8") as f:
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        text = text.replace("\x00", "")
        f.write(f"\n\n===== PAGE {i + 1} =====\n")
        f.write(text)
        try:
            imgs = list(page.images)
            f.write(f"\n--- IMAGES: {len(imgs)} ---\n")
            for j, im in enumerate(imgs):
                data = im.data or b""
                name = getattr(im, "name", None)
                w = getattr(im, "width", None)
                h = getattr(im, "height", None)
                head = data[:12].hex() if data else ""
                f.write(
                    f"img {j}: name={name} w={w} h={h} bytes={len(data)} head={head}\n"
                )
        except Exception as e:
            f.write(f"\n--- IMAGE ERR: {e} ---\n")
print("pages", len(reader.pages))
print("wrote", out)
