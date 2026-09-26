# -*- coding: utf-8 -*-
from pypdf import PdfReader

src = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Essential OMM\Block 4\Essential OMM - Cranial.pdf"
out = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Big lift\MedStep\_cranial_extract.txt"

reader = PdfReader(src)
parts = [f"PAGES: {len(reader.pages)}\n"]
for i, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    text = (text.replace("\u2018", "'").replace("\u2019", "'")
            .replace("\u201c", '"').replace("\u201d", '"')
            .replace("\u2013", "-").replace("\u2014", "-")
            .replace("\u00a0", " ").replace("\x00", ""))
    parts.append(f"\n===== PAGE {i+1} ({len(text)} chars) =====\n")
    parts.append(text)
    parts.append("\n")
    res = page.get("/Resources")
    if res is not None:
        res = res.get_object()
        xobj = res.get("/XObject")
        if xobj is not None:
            xobj = xobj.get_object()
            for name, obj in xobj.items():
                o = obj.get_object()
                if o.get("/Subtype") == "/Image":
                    w = int(o.get("/Width") or 0)
                    h = int(o.get("/Height") or 0)
                    if w > 80:
                        parts.append(f"[IMAGE {name} {w}x{h} {o.get('/Filter')}]\n")

data = "".join(parts)
with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write(data)
print(f"wrote {len(data)} chars, {len(reader.pages)} pages")
