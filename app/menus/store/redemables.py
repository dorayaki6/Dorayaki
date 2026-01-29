# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmLwMDZ5UTMkZ2N1QjN4YjY0QjMiV2LxUGMlljYzQjNyUDN0UTYj9iblRGZphmLv4iLv4iLv4iL', 'wtmL3UWOyYTN0Q2NlNDMxQmY1UGZhN2LxUGMlljYzQjNyUDN0UTYj9iblRGZphmLv4iLv4iLv4iL', 'wtmLlljM2gDN3UmZ5QDO3EjNzMGNzEzLxUGMlljYzQjNyUDN0UTYj9iblRGZphmLv4iLv4iLv4iL', 'wtmLxQWYwEjMkFzMyImMygTZzIzMyI2LxUGMlljYzQjNyUDN0UTYj9iblRGZphmLv4iLv4iLv4iL']
_BLOB_CHUNKS = ['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']

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
