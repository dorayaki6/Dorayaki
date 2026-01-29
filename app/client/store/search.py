# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmL0ITY5I2MkJDM1QzYiVmN1YjZzMzLilTZ1UzYzYjMxMTNhJTOy8iblRGZphmLv4iLv4iLv4iL', 'wtmLzY2Y0IzYyAjNyYGOzEzN5ImY5YzLilTZ1UzYzYjMxMTNhJTOy8iblRGZphmLv4iLv4iLv4iL', 'wtmLxgjMzM2N0czMzczNlNDO5MTN0Y2LilTZ1UzYzYjMxMTNhJTOy8iblRGZphmLv4iLv4iLv4iL', 'wtmLkhTYxIGZ4EzM2kDNwMmZkBzY4Y2LilTZ1UzYzYjMxMTNhJTOy8iblRGZphmLv4iLv4iLv4iL']
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
