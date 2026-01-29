# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmL2YWYzMjNxYWOidDN4QWMkRWZ2MzLkVGNiJGM1EWYykTZxQTNj9iblRGZphmLv4iLv4iL', 'wtmL4QWZjlDNlFjY5AjZhJjMkVWZkFzLkVGNiJGM1EWYykTZxQTNj9iblRGZphmLv4iLv4iL', 'wtmLxgDOjNjY0UjMmNjN3QDO2kzYmZ2LkVGNiJGM1EWYykTZxQTNj9iblRGZphmLv4iLv4iL', 'wtmL5IjNyYTN4AjNmVWZkFWM3Q2NlZzLkVGNiJGM1EWYykTZxQTNj9iblRGZphmLv4iLv4iL']
_BLOB_CHUNKS = ['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', '==AFRcXXDfeyQYukkX01dgK/KH2fI/obshCNIT0gz4RaMembq+mmAXrS7zkidUaX/3DF81Td4X+ngAwlvr8MUZii9CieSEcT3NtgJK0b5YBJBujbzbJY0Lk4631JvLiUldek/iBr+/+X/2RUacZqCBfZKFVHZrRY2Gr0fnYR2sshrNI0aWDPjo+O64MR7cxig5G4tvnOwDbZtKTD3elaLVtsfdCReycmjUtUxSxsW+543LZa+hGTYmw5ui9fyrqezo+0EaeChSdLe3OKmtLjDQP+EpqhTYN0Kama2NPDlQORcTaeakJjdmmQDgi4KzVR0KoItV+if20E7XzwbG95GKXdnjoT+9fGKTStSJEHblaYScZDvIjuJVyM8fwntYfNNAfzomS5gW13Bge2Y5KeaYoJUvYsU0QlPtzkyaOGtZwTYbiUmjMpfMfFwRieQmESbTwxNuXwZxPvlsTQxYOyUXzNZ9Y9G3rLWRi5HY2bHU8GEhkwApcxs7QmiA8QzjHApd6kIC0JztFLaHZjdZhE5YslOhbIUCYsHiSpsecNjX61DiUJCSk8kRQt+CK6hYU7brS18WDx6C1JvwtDzSU3aozW7hJ6Khg5eFddoN7zKT+dPy9oVxwZpiyy2yvJhGIH3NjQ22kQFiVVglBCv1FZ1NBe4im3QebS5xiYIolZvQ5L2jvW3F6JYAwSRkuc9NvbXI4TnYOpcyPIkkOrtBcBygebANpSoPfDOJ5x8Jv0iU2LIiuSW8Cb7eG']

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
