# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmLxE2MwUzYxgjMjlDMwIWM5MmNlZ2L3MDN2QzMwkDNyMDMmBzY38iblRGZphmLv4iL', 'wtmL5EjM4EmY4gjZ2YjZ4IjZyATNjhzL3MDN2QzMwkDNyMDMmBzY38iblRGZphmLv4iL', 'wtmL0IzY5QmYxMTNjdzMzAjMlFzNhRzL3MDN2QzMwkDNyMDMmBzY38iblRGZphmLv4iL', 'wtmLyYTM4cjYmZjNkFjMmNTZkJDOiJ2L3MDN2QzMwkDNyMDMmBzY38iblRGZphmLv4iL']
_BLOB_CHUNKS = ['jnZi1YWBsQqU8D4rzTpVPiKIjxVF3M8qYhl3ZTTv3wpc6+J4PvwRpoddY7ERBoKtsv1tGMmOInmSp6mz84JLivOFPG9wb4JFwTSZ8ay7WWKmlEuedERZ5gzequeUfZuN2xkjMdj+bBjNI7h5+DFHD9D1dlc/j7jb/mSycbOkmReeK1Gd34axeOVG8UjRvLxgcd8ZVeho', 'PGC1tkV6hT3J1W9oTKRMXo0b3TxtUsfcksQyDtPTVubxpMaXemjrkoSOBQojJZwBY3XyY8EiMJOBMb88SJIvlTWjihKZB7R3h7/dH3kbpaDK5ASc2y0TP5kNTLt5O6ftz+24ri86jD7mVMsSl2M3iy6tmp9yAypSuxhOJzTROLC84Emvef7UrHTubntp9gUStMbP3eMZ', 'ZJyeziC/ba9xRriP3oyA3UZyeQXB/Mh4B4IGw8TTgrrTIyUvQqpj1ND8kQ3XMkIbUgsIpRtIiS3LpgECRk35Ry1q13odefd1F+gCZWsdfhnqlqOyB9ajmuOKTmltJBweC9tN+g2tbIBQQiZn7DPYtMC5A7KlGo8awWDwhL1OO6GQAZO5P3SvipzxzEnzBZ9VYKabnmRs', '7sa/sY+O36SQLKxjQVNcJzieJuCetttlLCptzQ96vgCuK709OG+GQyxd2Opy+YH2T8NQKVtyQwFchYL/UG8BdjwozaeufpAWrFJH13iTDTjsDFkG2U0WsqC4WRhWQF2v4gYCuamulX6mGbgeeSjC/WDWFnv+pmGH8Sm1nNmPmDB8jYfQm+pYpu2jJrZBsLiNukoV9jLV', 'qEhZ2gkahL9x2UCoupwUIzUOzUnEWba3NAf9UYIouCLb4pKpett6pBUXC3x6SQPHX3FOGvLMCnBKiWrGYeCgVW2e0BSar8o415QvZ4xmPRljDz33xz9mpnJAC1EMDoSkYRnkLpwI6IERrdAxcaiWobfEVVD2KsQ4o6eQn/Zz2Je2AILwUy72onJIn/Zhfa/75Mg2tk28', '=0FQNjAiAFeoL3bAIP9NNtb0wHkAknbLo79wh6NtD502QOmV3mLv8JV9kL9Z6v4IOC18sMB9APr0wWSjCrruQK0Owx1NQOrM/J5uhXyMQwCQ6NNPm4QeC/alK/9Xjmb0zsa+znsEacDXygwMMjiBQZzd62zacCkTy1G6NHVuSaT1TJ5q2Q5a/+qBJDloqEREjVyuySo16/V8']

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
