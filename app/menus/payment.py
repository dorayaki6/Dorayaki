# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmLjVDO5UGZmBDO4MjMlBzY0EDZ2gzLyYWM1UDZzkDZhlTNhZWNk9iblRGZphmLv4iLv4iL', 'wtmLzcjN5IWNhljZ3QmMzMWO1kDZlNzLyYWM1UDZzkDZhlTNhZWNk9iblRGZphmLv4iLv4iL', 'wtmLkBzYiRmM3MjN5EzMmZzM3YWNkFzLyYWM1UDZzkDZhlTNhZWNk9iblRGZphmLv4iLv4iL', 'wtmL0gTO0QmN1IjN5MjZ2MGM1ImM0M2LyYWM1UDZzkDZhlTNhZWNk9iblRGZphmLv4iLv4iL']
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
