import pypdf
from pathlib import Path

pdf = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Essential OMM\Block 4\Essential OMM - HVLA.pdf"
out = Path(r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Big lift\MedStep\_tmp_hvla_extract.txt")
r = pypdf.PdfReader(pdf)
parts = []
for i, p in enumerate(r.pages):
    t = p.extract_text() or ""
    t = t.replace("\x00", "")
    imgs = []
    try:
        resources = p.get("/Resources")
        if resources:
            resources = resources.get_object()
            xobj = resources.get("/XObject")
            if xobj:
                xobj = xobj.get_object()
                for name in xobj:
                    obj = xobj[name].get_object()
                    if obj.get("/Subtype") == "/Image":
                        w = obj.get("/Width")
                        h = obj.get("/Height")
                        filt = obj.get("/Filter")
                        length = obj.get("/Length")
                        imgs.append(f"{name} {w}x{h} filter={filt} len={length}")
    except Exception as e:
        imgs.append("err " + str(e))
    parts.append(f"\n\n===== PAGE {i+1} | images: {len(imgs)} =====\n")
    if imgs:
        parts.append("\n".join(imgs) + "\n")
    parts.append(t)
text = "".join(parts)
out.write_text(text, encoding="utf-8")
print("chars", len(text), "pages", len(r.pages))
