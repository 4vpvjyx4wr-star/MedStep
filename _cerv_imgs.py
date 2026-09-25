from pypdf import PdfReader
import zlib, struct
src = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Essential OMM\Block 1\Essential OMM - The Cervical Region.pdf"
r = PdfReader(src)
base = r"c:\Users\jltiralongo0414\OneDrive - campbell.edu\Desktop\Big lift\MedStep"
want = {15: ("/X41", "/X42"), 16: ("/X48", "/X49", "/X50"), 17: ("/X57",)}
def png(path, data, w, h):
    def chunk(tag, payload):
        return struct.pack(">I", len(payload)) + tag + payload + struct.pack(">I", zlib.crc32(tag + payload) & 0xffffffff)
    rows = b"".join(b"\x00" + data[y*w*3:(y+1)*w*3] for y in range(h))
    out = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(rows, 6)) + chunk(b"IEND", b"")
    open(path, "wb").write(out)
for pi, names in want.items():
    xo = r.pages[pi]["/Resources"]["/XObject"].get_object()
    for name in names:
        o = xo[name].get_object()
        data = o.get_data()
        w, h = int(o["/Width"]), int(o["/Height"])
        tag = f"p{pi+1}_{name.replace('/','')}"
        if data[:2] == b"\xff\xd8":
            open(base + f"\\_cerv_{tag}.jpg", "wb").write(data)
            print("jpg", tag, len(data))
        elif len(data) == w * h * 3:
            png(base + f"\\_cerv_{tag}.png", data, w, h)
            print("png", tag, w, h)
        else:
            print("skip", tag, len(data), w, h)
