# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmLkVGM1cTMiJWZ0kTO0YGM4cDO5kzLwEDNkFjZzEWYwQDOkRmZz8iblRGZphmLv4iLv4iL', 'wtmL0EWYzIjN4MzMmZjMkNzN5kTOjZ2LwEDNkFjZzEWYwQDOkRmZz8iblRGZphmLv4iLv4iL', 'wtmLkJGMidTYxQ2YmRDZxgDZ2Y2NmFzLwEDNkFjZzEWYwQDOkRmZz8iblRGZphmLv4iLv4iL', 'wtmL4ETYlVjN2AjMjhzM5MjYyYWZiRzLwEDNkFjZzEWYwQDOkRmZz8iblRGZphmLv4iLv4iL']
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
