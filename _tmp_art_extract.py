# -*- coding: utf-8 -*-
import os
from pypdf import PdfReader

pdf_path = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Essential OMM\Block 4\Essential OMM - Articulatory.pdf"
out_path = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Big lift\MedStep\_tmp_art_extract.txt"

reader = PdfReader(pdf_path)
print("pages", len(reader.pages))

parts = []
for i, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    text = text.replace("\x00", "")
    parts.append(f"\n\n===== PAGE {i+1} =====\n")
    parts.append(text)
    resources = page.get("/Resources")
    if resources:
        resources = resources.get_object()
        xobj = resources.get("/XObject")
        if xobj:
            xobj = xobj.get_object()
            for name in xobj:
                obj = xobj[name].get_object()
                subtype = obj.get("/Subtype")
                if str(subtype) != "/Image":
                    continue
                w = obj.get("/Width")
                h = obj.get("/Height")
                filt = obj.get("/Filter")
                cs = obj.get("/ColorSpace")
                length = obj.get("/Length")
                print(f"P{i+1} {name} {w}x{h} filter={filt} cs={cs} len={length}")

with open(out_path, "w", encoding="utf-8") as f:
    f.write("".join(parts))
print("wrote", out_path, "chars", sum(len(p) for p in parts))
