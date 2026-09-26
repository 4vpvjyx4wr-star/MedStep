from pypdf import PdfReader

path = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Essential OMM\Essential OMM - EENT (Eyes, Ears, Nose, and Throat).pdf"
r = PdfReader(path)
for i, p in enumerate(r.pages):
    imgs = []
    res = p.get("/Resources")
    if res is not None:
        res = res.get_object()
        xobj = res.get("/XObject")
        if xobj is not None:
            xobj = xobj.get_object()
            for name, obj in xobj.items():
                o = obj.get_object()
                if o.get("/Subtype") == "/Image":
                    imgs.append(f"{name} {o.get('/Width')}x{o.get('/Height')}")
    print(f"page {i+1}: {imgs or 'none'}")
