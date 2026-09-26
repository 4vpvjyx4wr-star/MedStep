# -*- coding: utf-8 -*-
"""Dump embedded images and note whether any page looks like a chart."""
import os
from pypdf import PdfReader
from pypdf.generic import DictionaryObject

pdf_path = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Essential OMM\Block 5\Essential OMM - Chapman Reflex Points.pdf"
out_dir = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Big lift\MedStep\_tmp_chapman_img"
os.makedirs(out_dir, exist_ok=True)

reader = PdfReader(pdf_path)

def walk(obj, trail, seen, found):
    if obj is None:
        return
    try:
        obj = obj.get_object()
    except Exception:
        return
    ident = id(obj)
    if ident in seen:
        return
    seen.add(ident)
    if isinstance(obj, DictionaryObject):
        subtype = obj.get("/Subtype")
        if str(subtype) == "/Image":
            found.append((trail, obj))
            return
        for k, v in obj.items():
            walk(v, trail + "/" + str(k), seen, found)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk(v, trail + f"[{i}]", seen, found)

found = []
for i, page in enumerate(reader.pages):
    walk(page, f"page{i+1}", set(), found)

print("images", len(found))
for n, (trail, obj) in enumerate(found, 1):
    w = int(obj.get("/Width") or 0)
    h = int(obj.get("/Height") or 0)
    filt = obj.get("/Filter")
    data = obj.get_data() or b""
    filt_s = str(filt)
    print(f"{n} {trail} {w}x{h} filter={filt_s} bytes={len(data)}")
    if "DCTDecode" in filt_s:
        ext = "jpg"
        blob = data
    elif "JPXDecode" in filt_s:
        ext = "jp2"
        blob = data
    elif len(data) == w * h * 3 and w and h:
        # raw RGB -> PNG
        import zlib
        import struct

        def chunk(tag, payload):
            return struct.pack(">I", len(payload)) + tag + payload + struct.pack(">I", zlib.crc32(tag + payload) & 0xFFFFFFFF)

        raw = b"".join(b"\x00" + data[y * w * 3:(y + 1) * w * 3] for y in range(h))
        ihdr = struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)
        blob = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b"")
        ext = "png"
    else:
        ext = "bin"
        blob = data
    path = os.path.join(out_dir, f"img{n}.{ext}")
    with open(path, "wb") as f:
        f.write(blob)
    print(" wrote", path)
