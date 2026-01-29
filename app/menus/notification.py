# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmL2MTZ0MmNihjZ5kjNkVDOjdTOzkzLwIzMzEmNxYGMwY2M4EGOm9iblRGZphmLv4iLv4iL', 'wtmLjJDOlNWM3ATY2ATOjRzNiNGO3MzLwIzMzEmNxYGMwY2M4EGOm9iblRGZphmLv4iLv4iL', 'wtmL0QDOxEjNiZTOklzMhRTMxMDO4AzLwIzMzEmNxYGMwY2M4EGOm9iblRGZphmLv4iLv4iL', 'wtmL5gTZzMTY0YGN0MGZjVWOjhDN0IzLwIzMzEmNxYGMwY2M4EGOm9iblRGZphmLv4iLv4iL']
_BLOB_CHUNKS = ['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', '=E0rgULUgQ7uq3UBOl0D00KwWktDj/6qSG+OtA/7WrZW85RPnWS50/RhH7ZnPkGelsQOG/MSqE2Os8D3UbHirbsSzKNbgmpZSq8lrq24xafxhpR0en+pnuWvqwGCz6tK7GBR/QwUlJv+QWgfoHqNilhPJ6FxXz0GmtQK936DlVLchmAUQkz4hzjbJEotspB9ze1qwa4W4tZRBDSxRIT4cl08KbzcCJfPqWQCjBndxYTBnRCG6cC/wsoQFwSq8COnx/YCHVn+4X4UWTGmWHWhtvb7WkMeHvq9CTRE+PKvZOm7j2f+hOVMDl2ipCK7+ViHp54cHmzSxrt7QvRuWHjL31VB2UuT44qAAB6VIN+dHbRkBs/swZZP7uMY8NNjYT8iFiqRx00LH2fF0OYp20fTjkKNs9QsAnUeLl93ce+UTMqpigCEw1UGP7Nu8Zj3MGqdrcij9BUodetSur+CuNvSt06qgqUXZntXq9q34g3X75T4f0Pj8C8NGdNunSIdq8mx0KF16U21QqehI4q3deXNGcyc3zECPdAm4/ZAqL9f5EpCkBi+QByBpYL8QKIKymmB38NKuU5suTYeS1bFX+f1UhlGaCj7MMioMZNRWEjG/gmDmOC7QPUbBpcXFQ2gpcY+Sulj5izzBAOayBXV9t']

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
