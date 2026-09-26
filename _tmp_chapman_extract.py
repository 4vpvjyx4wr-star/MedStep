# -*- coding: utf-8 -*-
import os
from pypdf import PdfReader
from pypdf.generic import DictionaryObject, IndirectObject

pdf_path = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Essential OMM\Block 5\Essential OMM - Chapman Reflex Points.pdf"
out_path = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Big lift\MedStep\_tmp_chapman_extract.txt"

reader = PdfReader(pdf_path)
parts = []
parts.append(f"pages={len(reader.pages)}\n")
for i, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    text = text.replace("\x00", "")
    parts.append(f"\n===== PAGE {i+1} =====\n")
    parts.append(text)
    parts.append("\n--- RESOURCES ---\n")
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
                    parts.append(f"{name} subtype={subtype}\n")
                    continue
                w = obj.get("/Width")
                h = obj.get("/Height")
                filt = obj.get("/Filter")
                cs = obj.get("/ColorSpace")
                bpc = obj.get("/BitsPerComponent")
                data = obj.get_data()
                parts.append(
                    f"{name} image w={w} h={h} filter={filt} cs={cs} bpc={bpc} bytes={len(data) if data else 0}\n"
                )
        else:
            parts.append("no xobject\n")
    else:
        parts.append("no resources\n")

with open(out_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("".join(parts).replace("\x00", ""))
print("wrote", out_path, "chars", sum(len(p) for p in parts))
