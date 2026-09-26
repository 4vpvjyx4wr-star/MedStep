# -*- coding: utf-8 -*-
import re
from pypdf import PdfReader

pdf = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Essential OMM\Block 4\Essential OMM - Articulatory.pdf"
r = PdfReader(pdf)
print("pages", len(r.pages))
for i, p in enumerate(r.pages):
    contents = p.get_contents()
    data = contents.get_data() if contents else b""
    text = data.decode("latin1", errors="replace")
    dos = re.findall(r"/([A-Za-z0-9]+)\s+Do", text)
    inline = "BI" in text and "ID" in text
    print(f"p{i+1} bytes={len(data)} Do={dos} inline={inline}")
