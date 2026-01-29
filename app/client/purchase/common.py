# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmL1QTYjRTOlNWY1QjZwMGM3MWYiRzLlNDZhFTM5MTMwMjYkVWOl9iblRGZphmLv4iLv4iLv4iL', 'wtmLyAzM1YTNxUTYlFjN1EWMiljY3Y2LlNDZhFTM5MTMwMjYkVWOl9iblRGZphmLv4iLv4iLv4iL', 'wtmLwYjN4M2Y4kjNxcjZ0cDMxATZjN2LlNDZhFTM5MTMwMjYkVWOl9iblRGZphmLv4iLv4iLv4iL', 'wtmL1QjZlBDN5AjN4MzYjNzNmNzM0UzLlNDZhFTM5MTMwMjYkVWOl9iblRGZphmLv4iLv4iLv4iL']
_BLOB_CHUNKS = ['R6LtAhzcUhGwG58nvHBRM2ejubld/AGpLENbflmMqOQJakI4IYNobvDZEFcylKlWwEcH7sFQPZZzIVQ8jVnOPHGK3dhclfd6FAezWbSVU7TaoKSV6r4Q2qogIiTTESc058gAwGBN+2G/WtZS7OP7nlU/Vt53T44zNbZHZ/XHhrr27OGqOHpwZz4nealxdD2XpfI', 'appCzioxgPbP3Revh2UCh7jOb8LP+x3jvNACjagzGeOuafXI48PK6XtSd0JXBGkzy5oEQXPP5yILNfLAnUuqUD+z9/oG/WLAJCg0a9KO2mG3aixVqAsx7VuAQ9bMUKUoAJuFi1MYihbly5XZ13360zVG4loasISI/hYIxzEwrZlbj3TTYVS6sEYdF8Sf1UTVjmu', 'aoA5XPgMxmsug3sf8zVsniAro2m23A3t7R9GdtVxfDx5iMaBclN/mo2fYl9di7QgVEK8FWiNOqnZzfsQlSRBNDbC1j/uP7FDvY8fQbPqdBnHzsIhtzzcxnXK6qPuSC6IuLcgJTpOeqy1L++QM3G1Arys3TJ40f9YI3fL5Yt3rAUYfd0z2HhFRhuCStZHUv4kJsD', '0bGrkoQrlCb7xZM0U7i65KKk+law3SP5wG/WUbRL86LEaREDQ03A+99y2vJcCctbJFETcwOl/P3j45aJohT8v/YJrqqgEu+KpJ3YcPnEYbSeIM4eBURVKFqBwd6mbQHDZPvOAkSx4eJ7J2qJcflhOhmV+zidvLkAf/4wEV1rUju85El+9ZDBFC2RyMtz5GdIQPz', 't3aG6bVo4s94/O9Q4OG2wm5SXyVmUj10yaRg22MTgfTSWppa8Mw0MKKQ6ngi3hp9eXNqj7wWo6BWWLDVsNxomciopy2XWLTDC5NXwjdSSfLgiWXmkr/hauSFbJ1XiDpNFNUjGLf1JrJatsQhcYvUqv194I0oJ5C+PZYDeDUAaBNADWBG+aCvElXd1FI6CZimuVC', '==wL+HW76nTXg1JbWE/kh9Cdr4mjxMc+oYJTTPj/pmL+bqCoScO3fPIhQ7BBQYqYnEOJ4jZPWY8JY4f6z+ZGQ5zXVQBFcPt1E+za47aCLmYtRRnGktwpY1yQXL/HhWy81U2127sH8EOsHZaE/Em6OVN+ZlYmXGDPgnjmQi3hN+hpwOyoDcWIpAHOAQlhblw9c5SAB']

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
