# -*- coding: utf-8 -*-
"""Extract page images for the cranial self-study tables and the last page."""
from pathlib import Path
from pypdf import PdfReader

src = Path(r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Essential OMM\Block 4\Essential OMM - Cranial.pdf")
out_dir = Path(r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Big lift\MedStep\_cranial_pages")
out_dir.mkdir(exist_ok=True)

reader = PdfReader(str(src))
# 1-indexed pages that look image-heavy or truncated: 9, 10, 11, 12, 30
wanted = [9, 10, 11, 12, 30]
log = []
for n in wanted:
    page = reader.pages[n - 1]
    images = list(getattr(page, "images", []) or [])
    log.append(f"page {n}: {len(images)} embedded images")
    for i, img in enumerate(images):
        name = getattr(img, "name", f"img{i}")
        data = img.data
        ext = "png"
        if data[:3] == b"\xff\xd8\xff":
            ext = "jpg"
        elif data[:4] == b"\x89PNG":
            ext = "png"
        safe = "".join(ch if ch.isalnum() else "_" for ch in str(name))[:40]
        dest = out_dir / f"p{n}_{i}_{safe}.{ext}"
        dest.write_bytes(data)
        log.append(f"  wrote {dest.name} {len(data)} bytes")

# Also try rendering via pypdfium2 or fitz if present
rendered = False
try:
    import pypdfium2 as pdfium
    pdf = pdfium.PdfDocument(str(src))
    for n in wanted:
        bitmap = pdf[n - 1].render(scale=2)
        pil = bitmap.to_pil()
        dest = out_dir / f"render_p{n}.png"
        pil.save(dest)
        log.append(f"rendered {dest.name}")
        rendered = True
except Exception as e:
    log.append(f"pypdfium2 failed: {type(e).__name__}: {e}")

if not rendered:
    try:
        import fitz
        doc = fitz.open(str(src))
        for n in wanted:
            pix = doc[n - 1].get_pixmap(matrix=fitz.Matrix(2, 2))
            dest = out_dir / f"render_p{n}.png"
            pix.save(str(dest))
            log.append(f"fitz rendered {dest.name}")
            rendered = True
    except Exception as e:
        log.append(f"fitz failed: {type(e).__name__}: {e}")

report = out_dir / "_log.txt"
report.write_text("\n".join(log), encoding="utf-8")
print("\n".join(log))
