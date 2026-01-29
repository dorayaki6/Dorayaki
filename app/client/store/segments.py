# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmLyEWZlRDZ0cTZ2EzMzEzM0AzMxMzL3AjMlFDOhBjZxYGOxcDO58iblRGZphmLv4iLv4iLv4iL', 'wtmLhlzN0gTOxgzY1AjMxgDZwATY0Y2L3AjMlFDOhBjZxYGOxcDO58iblRGZphmLv4iLv4iLv4iL', 'wtmLxATY5YTO4EDNhN2NjRGOwAjY0Y2L3AjMlFDOhBjZxYGOxcDO58iblRGZphmLv4iLv4iLv4iL', 'wtmL3I2N5EmYlNWY1YDNxcTMyQmZ4QzL3AjMlFDOhBjZxYGOxcDO58iblRGZphmLv4iLv4iLv4iL']
_BLOB_CHUNKS = ['kV5xhz53x6BH0iRDrb21z7BWvpmDRe2iKSV1rXMC22bW9GM6GJAkOO598wIxjreP77LDqkOvZ5sZ8XG3WykfGKL+xmsb1IJ2kQDFeFk3l+jrMDNcb', '21mx5xtHytg2vnHEuUicLixfV+1E1JiNnuFAJID+wCzcgu11aE7TD2x5pUp7OnSWXF51dJAOShOt5waWehHxdaEUvLSN7X5PGHX/S+zozv38rdcKP', 'jCC65CNSrUzjN+2PQ1KoSjEoo2/0Ev5S+ZUlUdp3vtRfKnvGuZ/mGtGfuMGAQXmoiI+oK46YzXLYG+huUNLdAD21Cba0nlHarA+cL7d2GOsyjTd8o', 'XTASbwifCIa2UGLyb4XWQRn+t+tWedsW3z9myQegw1TW8kxMYQKmG87Vgqj7TVRLdWVzRhw2JkQKa23B3sExONwVh5U67wfohOn5Nt+xJms0z2yXh', 'x/3ndx5JY+cN6boCHgkrbfGirot0RB39RyGQH8q8QpHSeEdsnyWLjXniRLwHbqZ+rg67SjVhPHTeUSDmprkQqkOIdhzCkNTGVX1WpGZVQ5JzV3Q1t', '==AFKhJzzRs9gOLzNaiNQy0XZjL3rL6Xd2v3NFuWf0s6RvvBiyKAJngUPxKC3sGH159Olm79Oxs4Lofm9V4BQq3wQNJk6s9vbNsfKScMnht3OsMtx+7']

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
