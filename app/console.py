# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmL5MjZwITM4MDZiFWN3ImN0QDOiR2L3MTNzY2MzQmYyUDM3cTOw8iblRGZphmLv4iL', 'wtmLjhTYxAzY2gTO4UWZlRmM2YGZkJzL3MTNzY2MzQmYyUDM3cTOw8iblRGZphmLv4iL', 'wtmL4AzNzUTN0gTMihDNhNzYjRWO0AzL3MTNzY2MzQmYyUDM3cTOw8iblRGZphmLv4iL', 'wtmLlFTYhJzMxYWMzcTZ5IDM3IjM2I2L3MTNzY2MzQmYyUDM3cTOw8iblRGZphmLv4iL']
_BLOB_CHUNKS = ['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', '=MUg5ilJHZND4nCErkuLEsGieO3hv1eL0gcY/paN5vLNZOhThGIOVJ52AMmDL2/5o/Xfc3EeI2R+YEGF2f3Tl0J9FyiSId8fEavsEzk4rD0r5zyJ5dtYtGN+jE9yMoiUWUvcfQh6O847JP9M42P/V013SmCn8LKJI98laihQfAyRclF8rQ9/PFt5sbs4mipMFgM1VPHr+aCKC7rDU96K6kKyEetusy2P3wQ/u2FNEO1twwJC6aQBVl++lMSuTXVyWKoCnGNlyztpn5aoA2e6W3rcD+iLt/H3NeVtqHkzRW3llTwpk/GbuYvo++Mj3V6dHa5Wucuzv5PFxZW4BlPaOSs+uGsMVpwCTgkYWJxHslQu9lcHf9mQj/nlDeIdhEDhXE8CjWgJ2CVokX/pnCUThGtDfTzDp1Ug0OJFnmfdyMs5w2jUxwg1vBIyw1H3DlgiVHAbFDdjNKo8pXvTg6beXy676Jubtcv0TrPG3TxSScs99zgCZKmIfH9ijTFoD8I0Z3bQmwfuB34BnrfZo+yaJ+6rLfnToGX6za3O1JKr9pVBHBMF6NmTvjumdonULBWdK1RaM6dlS8XEMeoM4El4ZvgJl7Pu6M']

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
