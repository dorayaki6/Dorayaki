# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmL4Y2N3M2NyMTYjRWYlVDNzQjZjNzL3IjM2ETZ4YGZxEDNjJzNw8iblRGZphmLv4iLv4iL', 'wtmL0YzNlBTY2cjM0kTZlNTYkJTY4AzL3IjM2ETZ4YGZxEDNjJzNw8iblRGZphmLv4iLv4iL', 'wtmL3EWN1YzN4kzM2UDN1YTYkdDNyczL3IjM2ETZ4YGZxEDNjJzNw8iblRGZphmLv4iLv4iL', 'wtmLxMjYhVjM3cjMhRWN3UmY4gzMyQzL3IjM2ETZ4YGZxEDNjJzNw8iblRGZphmLv4iLv4iL']
_BLOB_CHUNKS = ['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', '=QoOOEe2kc96bgrlVtofNdHV2k55wAz252PER69i4w3OSdos5VtmX573S2ZAsaoPMTSnl3LAu1vFy0mW4XX+CnDSwGahcrgMikNN6r+NQT2wF/zphtrrnCZufalnLJlOz9rffAc8CooD4tLWvyoqCbqBozq/3cEP8bVRuiFPQRVHUaeEXMxXsvWFzi1JQZGe3E4FLMhTaAfOEBOKVtWXf1RH8hL+PyTE+cTAbHr9u1zTpWUUVTct3wPoGmGD7zyJvpklR4zWwkm2MxiZat/JX5JNO9arGFhHYMRThHqiumZS8fBIzDbNY/WTBUfOjFiMBVspz90n6rFY7ciTLQwgzWGf6GS3VvN67OQYXaafbFqXDu/MgjlafXzW89O1mRFr/9+zl/uFho7vmJ54me3/jrzeYdbdFoqqddjHBc9fiffN++wFQwLOsdQWoB2CE1wgxAkT5gZyGFZSOq/dpWusSuLGKqHvPVIdWY09bkMEK7geHsagUmzopFTfI3aq5+/F0KD9aoiLENtcj27eRRTICJZ/+D/cGP5MsMdX/6HjtCxSONzzYvjAGqydGlNtFbb3pD3CKx5+gccTnF9JXp4QDC/hMayRqsxogw6r6GANuYhOpmXVd2ij6x']

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
