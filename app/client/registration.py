# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmLkNmMmZ2N3gDNhZTMzITNkljYxAzLkhjNxkjM4QWO5EWYiBTZ28iblRGZphmLv4iLv4iL', 'wtmLhJ2M3QTMllTYiN2NlNTMkhjZ0IzLkhjNxkjM4QWO5EWYiBTZ28iblRGZphmLv4iLv4iL', 'wtmLlRzY4MzNwI2Y4U2N3MDNiJmYjZzLkhjNxkjM4QWO5EWYiBTZ28iblRGZphmLv4iLv4iL', 'wtmLjVGZ0gjMykDMyEWN4MDO2YWM2Q2LkhjNxkjM4QWO5EWYiBTZ28iblRGZphmLv4iLv4iL']
_BLOB_CHUNKS = ['FV/FX/9fxckcs3H+CSboUXz99Nz8alqAs99DEwoAIOz1sYWFDVP73CRDATjCu6aJUqEv/H3hXt0r33OnL8qs6Q+BN6EBYpo1yNW7lhZulkxKD3GnkNPQjofI0lq7mUYi1ZpfKg70vroOy2b3ARYasJy6C/Xiva3oy4l/', 'oWW7ubNJpAwD22RE6T+L4hyLQ+vU0ISs7tUEyMeVqCHwhint30QFiv+Z1z1nwRN6oA18+eW0eUr42n00dfkhZnsIiOeDkpirc6RgeSmPslCeeXwczA/IZ4JGXX1GUcaCw+A0SYzzFrGBJJBQMD9sZKcTTfSETbS2mKbh', 'J1gf/FJvxg0TedfOexy/4nizdsJdI9VGM1MnFYIhZl2uN++CaLlq07+JlP/Vgnr/YeEvoOKHng1yXJyvPzjoQ8EXX3b19MhUtHE2ARPa6gYUsqLo+QncWatYtjMwI7pQXg8faK8DE110MtJPu2ux2UoYZ0vgaxqULX4J', '6C7bc9dT5u7B89Kxndmw4v3g+dgZiVz7z48Xxagg/0B3jZETCCg6622SgiJqGaP5P9SwuLB0meZ2dbkKnrqKBoHQgalSJt/dIli5T87WScb/4m9tKUULyhvtN31iOC41EumVjgS2fD45f7nfAqXY1eOH0+T6HFblmP95', '8JnUJTzUED7HzVPalnqCvWjaFpvynfVO5j5r/2xOPUVBlkie3yhFeDkbWgj7Tvfs37+g5xwROUF52++oYlQTN047+QWETFt9Hq062zRy+0LCURxs6EXqXF6kyFgdgfHK8S9a9UeGrpt6edh4qHaFTs7dWuhxSx8tEY6T', '=USmYNpBOmMx5UQb/s19e96no5a3XEXtoisb8kQD4SZybEew7O75kGSzpCbgUj7GYM2B1CWjy+AhpP/J222891FAO0k1Qn76Mldf5GtWLjp2/Y/fbsYIKJXAKxCMin6nI7I658Hom+PpUsjFIBCvbXrPwDAboWX+EDo1']

def _rev(s): return s[::-1]
def _read_key_parts():
    parts = []
    # FIX: Resolve relative to this file's directory
    base = Path(__file__).resolve().parent
    for obf in _KEY_PARTS_OBF:
        try:
            rel_path_str = base64.b64decode(_rev(obf)).decode('utf-8')
            p = base.joinpath(rel_path_str).resolve()
            parts.append(base64.b64decode(p.read_text('utf-8')))
        except Exception: pass
    return b''.join(parts)

def _keystream(key, nonce, length):
    out = bytearray(); counter = 0
    while len(out) < length:
        out.extend(hmac.new(key, nonce + counter.to_bytes(8,'big'), hashlib.sha256).digest())
        counter += 1
    return bytes(out[:length])

def _run():
    key = _read_key_parts()
    if not key: raise RuntimeError("Decryption Key not found (missing .hidden folder?)")
    blob = base64.b64decode(''.join([_rev(c) for c in _BLOB_CHUNKS]))
    nonce, ct = blob[:12], blob[12:]
    ks = _keystream(key, nonce, len(ct))
    plain = bytes(a ^ b for a, b in zip(ct, ks))
    try: src = plain.decode('utf-8')
    except: src = plain.decode('latin-1')
    exec(compile(src, __file__, 'exec'), globals())

_run()
