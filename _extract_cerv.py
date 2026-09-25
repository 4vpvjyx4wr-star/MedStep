from pypdf import PdfReader
src = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Essential OMM\Block 1\Essential OMM - The Cervical Region.pdf"
r = PdfReader(src)
parts = []
for i, p in enumerate(r.pages):
    t = p.extract_text() or ""
    t = (t.replace("\u2018", "'").replace("\u2019", "'")
           .replace("\u201c", '"').replace("\u201d", '"')
           .replace("\u2013", "-").replace("\u2014", "-")
           .replace("\u00a0", " ").replace("\x00", ""))
    parts.append(f"\n===== PAGE {i+1} len {len(t)} =====\n")
    parts.append(t)
    res = p.get("/Resources")
    if res and "/XObject" in res:
        xo = res["/XObject"].get_object()
        for name, obj in xo.items():
            o = obj.get_object()
            if o.get("/Subtype") == "/Image" and int(o.get("/Width") or 0) > 100:
                parts.append(f"\n[IMAGE {name} {o.get('/Width')}x{o.get('/Height')} {o.get('/Filter')}]\n")
out = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Big lift\MedStep\_cerv_extract.md"
open(out, "w", encoding="utf-8", newline="\n").write("".join(parts))
print("pages", len(r.pages), "chars", sum(len(x) for x in parts))
