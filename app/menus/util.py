# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmLiV2M0kTY3cjM5cTY1YGMmNzN0M2LhVWZxEWM5EGOyYDMkdDMz8iblRGZphmLv4iLv4iL', 'wtmL0EGO5MWZ0gzM5I2MiR2N0gzN1AzLhVWZxEWM5EGOyYDMkdDMz8iblRGZphmLv4iLv4iL', 'wtmLhRDMyUmNmRDM0MzM3AjNjZDMzQzLhVWZxEWM5EGOyYDMkdDMz8iblRGZphmLv4iLv4iL', 'wtmLzITOhFGN3MzNyIjNhJGNxQDMiV2LhVWZxEWM5EGOyYDMkdDMz8iblRGZphmLv4iLv4iL']
_BLOB_CHUNKS = ['f2T6iRi2LHGwymmfhk5yZTZyYywM4OGSbPo5yEtqaaQRj2aRFJfNDYrjUMhVsc7mos5F2aoIaLlIRtx5J0K0u4ld/42ov0Fdj5qgYlSBj0kNAHHep2Fmg2oolvf+HuFX3mnBE++yUvdI+MbQUhduLUQV3XZWqwaj181sw84WI8wfm+/ntyja9cYo6tEBk86LxIzc3o5EovbmLE+GQPTYsWy8pe9cN5nB3uDkI16ju2MVIgKwC3WJj7rlNT9Ad4yqaUW3LJ41iwXzVpzryTZyIhga0m2gyOuCgfeQ4opUDGBeohHIOhDNAbtPMcEOG2hdgDtt+wJVF3FXot7MNCypkLNAByJMk5F7hKO6Wl10ZWYv3Xdr8GVXMLKdOthS', 'QM1nQAyFEFy7NsCKytnS/z7gkP1W4H/WPNK7PACqR2oOeOSQzepqXwzN+pD1rp0ZJCVtbTUIpirycPIrzLGQy796Ga6jPNyEIraS5UDVZk/Kf15Wxc0Vl42TRj4Vl9fPyt1fixW7VnX85P1n9m0AVrh1wnQMpwiVAWeQ6wzIuVawjFT3vPBLjbbpCFokgMV2YDzVVbD9wYT/Xlq4Y+FjTdAIMl/6mLdeGpOiyIdPxqIkNYFNM85TbLhMsoTAOHq0XhrIItks7IqxoBvu+WlDCr2FDUfFCsl3QDiqEr5IJHkF9G1POEJc5zV98GU3W6hgFP/gjIbNVkOEjXrcC85bY0BxHORHSHRuFc3pQMA8aofz+eATnlzUea6ELjDt', 'Mjq7aAMLeATsMbD/PkP9+8FpqZ2VSlD3GfuVt4vr5r4sA/FDIqWz4g1OiAJ9p4H1H6Fv3tLPElol/ZyqvEJdsoKF83G0bWbwcY4g8H2vU2akAXutkCGK5skg14HnwOBYLIPlPOeYyp5TnSm1PSfHyTOb7qFnXOxZM4a8ItwVnPoyOBIqsgzTCUwMTqRbdZCyVTtiPueCR12kS+jMfCH8go6g17HoH1yDAQ0sJTuS/YtemBxnXJMkmYdXy38G7A2qhKTIcAzRqWDcVa+XOS1UwEVAx9TogLqQBEqMzWCzyj5G24XJ1mXDb8yXUMb+0H7DdV6FCeh+mXCpbyr/BcD9yQwPuSEc3kLSwTTkVObZCzoOTsnsRPUGaKw09oiL', 'NzNpUyJQhAgCmuPBlZYG0vWJhl9lGz8xrU1pDmaOfkh/VVDtj4HPP1TIoDPbw2XRBloJvBZGovmAo0JpwzEoXVxaHNWvgAwwKr1Rpqz7W2wvTGEJgwuXtIdV4kaKjKAff0ijhpupHsPByCDKBUDmoXWoYwGmteNtrnKCpQSL0vlnK84l3CLYTuXWcv/xEG0BCQul/7q05zuP2t/WgPDYzo1OKm043fRPqkldCN794I6KZ4ObUSomnab/ak7GndyiOtSt54eAEdr9tuKzihw0tojwuzIl3SYPwqgClRMlCBXEOcvlTfH5sVAqRRoPauvDuJJ2/CVSdw6ATKHozGwcBPtk1kubb67l1X4j4knOV9fHYvWM/niUcCPAQpCb', 'yJrOkkEZfCbUmcfX01VRrgHkEewSmT17yJo5jsCSQU47zXFCogiNoFLdyEuw6KzG0kd81GxrtpgHzLGAT/TNVinD2pVdHeJSWWvElBOH9Ez6JIbVGILbIjeG8toH3Kb6L8ur/DZFhCXY8DYmjE4akzvxzleRler7pieDACYYVXJro8gLemhcCTSSkrCPvnY+M8/v09AytBl04Oy2Ve0I6iNDySf5l2CqRUpc3Mg6J9fh8LPB0ImxKqiM4kVFGZutFP/KyRwFRObbTQy3H3bRLk6Gp7aIrcbrbwLaN2OqfdpAOJ+CgkQg1+VGY0eQ+NWgrQcq7w/Z7WPXICqvehEmTSbsFZ9pNBCRAMaAF1TqUqBiqO7XLiRDeTCrkSqh', '=gb4jhd3bz00OpqAg8hvy1kAY0ABvdwrgcUS2Zfvtr0Hud9aXuIzaNZuv6qJRUBt+3MMQAcJZRsv69PTdpYozGgEXVLHfHYOhxeC7VYFqxyQuUro0vbFl2OHbAEkaxJevuOOQi9/gOqjYsrz0BOq2AxFtD5cy/iF7FZF83hKfrjtFJ7Gn/EmoTg9oagtJ5CzgWYS7G6iC27Jx9lk/Q7Pbk1RXBZJmY4gJQkT0SXhF/YcovrxuKIjzbHUOmuEpP4cZoJi0YRU3z+3anzMVlF5cdinrbsE7Neu18ZattPGDbB37BG4jMDo7awWMbv9jc+AFp16aPj76ZV1KM+vq91tndtLqukAP37KavxCoeMvPkzbGqtxuQugOjDChU8mnrsQ']

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
