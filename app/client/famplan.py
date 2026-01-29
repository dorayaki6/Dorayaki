# Dorayaki Obfuscated Stub
import base64, os, hashlib, hmac
from pathlib import Path

_KEY_PARTS_OBF = ['wtmLxIjMkZGMxYmY0gDO2kjNxQGMwMzLxImNilTN3AzNzMDZzETYh9iblRGZphmLv4iLv4iL', 'wtmL2UWNlFGZiBjYhNGM2MWZzQmZ0YzLxImNilTN3AzNzMDZzETYh9iblRGZphmLv4iLv4iL', 'wtmLmZGMmNGZzEDMjZWNkhDMyETO0QzLxImNilTN3AzNzMDZzETYh9iblRGZphmLv4iLv4iL', 'wtmLyQTO5UmMlN2N1QDNlFGO1kDO1Q2LxImNilTN3AzNzMDZzETYh9iblRGZphmLv4iLv4iL']
_BLOB_CHUNKS = ['TfwwpdbNVVWV8p5SnJaBS0kcYF1gvwqQ/e92a2xMmefQTQgKJ4cW2X4s0dagBj39Gq0IzlTbquxLQlo542xbLAUZPYIELAA3C+iBjfjR6m5dAGFkYH0GemKByYC+pqNBDH5m0K7EVbqKYxfrHYOED/a+g7vfzDGnM50BkqOelbEiq0yzhQpaz8ZRNXurjT16pJ82Is9Vsb5LTe/07cLXAXpcZLZUa6pYF5S+TSukiIHfymUUTf3qg7UVOfBBxFr01jcoqXyzXadEN7luBPOFXzLuU43aodrXzoul8ixfPyJyMHP9QAdVQICiNc9S1zjPXoNOSknVd+s2d5k9tc0tLr/6USROKraIEsAUjiRsj/Z9Wb5TqOFYhT1TUxnsxWnPFxWYbnRSG/pj+ZoNmdc95dTArW0dsCGXzg0hxflr2zZYZBj2/G2r3rzpRO2d0v6NSTk7ljz6f7vUNcgil5NA0Pz89jfESmlNJ8kPLDwq2efV70GGCt2EVh5AmVoAIThBsiyrpMcEjjjkcOHgPaBt8jF7066drKGYfoPlMs0WESeSI52ZbchKU+VPe8bFQAgE62ZG10FxQHnJ2MWxosdMlvy1pxRSStHzd3FSAeS3Ps882vdB/pX+1vmQ4tUhdd/bKD6mLJa7ghbdyqGb5I/t0sIv4b18OF5mYvZu4Fbb3nKXN3GmXsqFvFlq6S/2/o0CgTi4fDvrl4fvQs4HDuQxDPI0gcGUG5YBCkqS6XNega+HkG+CDGF4LjWwJ80VnueIDzdTZNIDm99z4tMNt7tCh45ioilkb0hdN7Wnj4aUtHo8SrjKmBgHnGiP4Q1IaiY5HnWOY5VPe6duDQdH51orxZehDy', 'PoI8tPCKreroAFw25Q0FuBOAM+/Mf/ybfJ1tdD+ssGa3hid3bYmNzinTVB0wDLPw3y8xwio8ZTVGNcoSFYNPZnFX/As6DaEnQsH61Rqy08i3PqotG/VQL/WOm7VFGQBLXNcgarfo5G/uDhlLX8H8/B0YtyQf2jGmtHaQxG68BvPyPxBbUrIxyx//T8iG0Kf4n4bKAFkwfeo9z/Xf8yuwj8ProkukFi7/oXi4gieAOju1w+JJEDMSUujqr0PugZya7GjF4Hpgi3GmTvwWbKpHbDtbV7s5EX7hvPc2jIrhEd++WD+iW3zEck9e0JBbJ6yJbSMCgvZqJ/PdXTR2kIJYyUUgBm8mgtYBss+hGKk1raHRfGpHWHWxqPJNOgdVXciJq0nXnqOduoJPCi8LVyBsUmkIFFGRkkK/9nWX/zWnwn7XThw1fzQ4JV8UfqDQp9EfZ1Puy0rVRcsKB780RXWtGj01tfb29MPXFCrWaQw9FR0/AqZvdoivQGe7yZPF/Q+jdaJ5G7tgqGjbZhFhdggKJFvz/8vDEC5trlBuaYC6w5LtxOFcJJppqkd211jjoJfxcx4mEn0v7rx/ljnKnT009aRlbnU4PGlE3wYvHNS4337gzuCu03ZMy5VuB0HPNFCAJnN0fDMhhhB/VdPUOTdCkHIePgrhoDjP4DGb5fr2arm1/usEVKVE1wqQ6gchnYzvxD1FA09m/mq2Z7tM79RXnP6L5YaxZj/S8NEdRM11NmOmM2ytfkKRwELA/Zbds9RyOwfQTukkeh+DVW0GoZQDRxJXhl3kVnsGu/NVseg7PK+X8RTNdEd5p3m/ONjOJiWAcCBOREAcOk4vxnjueua4UioGe6', 'RMaRUfSlGjVXS6DGuZGfxkwLafJTCHzP2RcT/nDYKzj9SANKV/AfKvoHHjRpBGpVwOgRBiTL5TxFHGYB+xQASDNg8aglAiDOBVHorpazyCtZ978IogKvg0sOHwzbe/JJ19murE/I/A0Ph1HIU87INEZDKMHB3s66PebIYyaM2sR69XE4As2WxjOgD60AL191fi6ZyLMnKSERf8w4EBwUdp5NTpiBVP/xrYHB0zcW9A2cdSU4oNkUlkbSvfiwiUKc2t5HUyEloneyNEYv0hUbAB6XLKHRxC9d8fOG1bN4k4WIHQVqzWM8F9/4G5NAHq48ZBTgHyEkHnusbUtFvCdryxIYlIhl8ISe98viVwHfLgmcWpcZpKBzPOwMVDQPVv4O3iSYw/p6pwpZrCsgInaHi5tywbc4v9dlBwWIiQkHeKAgfPrhXAnqlA6qFja9rwZnkJlLKlQXRAUM7ukxBkpow2HjuPS5vzPa2UX46Ki9tA5hX4PXd/s4CWLOq+7o2HZ+FKZu2gRrj8vaLMHuZyZ3W5vPkwnSonmrQIbyf5jJWBJWMVshp77cxjxknlKWHvY4RnYUEjMfNJ6nWSeqYGavlSpZjS8OiCc22MUYMRumFgO9vFZqs/POwqCFs7mzZ1t9Z64Tj1+4j1XpWpm26hOgNGKrMKJ+H4NIlZz3brwpjlmoKjTfFn3xVqh+0xpV+NOdyTn5li5fHdwZfgmY56ZwSGf+cTNLBHek58iTBJCsFYtNdUmHh8NaPTsJMGTuoz3uymJ1hsrfn5wFn4keaUi51+drC4wQPPnJA+BsOl3utT4VNGSgk9ei3YGz58FTtD7PqepQBu1zczKHcjnJN02akMeaho', 'H2JGV84qofdtlIYwF2rx8E64+GyD0xOHdi5mqG5OuCwAXPir0CyPmsXbEFeZAA+ohwbf6KzZnx6QJfxRowD5FnrlpwN4m7IjEJPLS6OC8yfZwzi6Sj53x38zAstqP7QkjLNNN7XoTPUNaTA/IsoquGymltBYLdw9Hpro07RyNn0AyuEgjWI3ieozfrzIf+K5Y5IMvVozx2QgtpI0WMp9OC0XSO8eUxQCi+c98ZPhLxzyW9KlUyemecH9S4zXV48YTVtyKnTD345Yj0RcbmkIDTHOGftDk3bumWE8ztVy1Nt+WFscuf8C+QOSc0ETX/6K+6JbBQjMQkNA3okQcYrj9BGeJuqXhvrxje8ry2JQ6WuNt58JCFeAh7wmOZzl1XdeezOD5ibeKszq1d+pStWiqzB0VDddQuQCNxAGeldcinkNC0D5z8HXbY0zvixvHrWJdDg2AXLGZEDqn6uyoWmI6senfExq0HMmoOd/TrxnQ8FqMUEq/v6VOhchiMS/59WDYV0C1ie0S6YLUWW0aSiM+kUbmJdJ+DHOWyKLqqb3viHWgl/qN6+VpGbYwFItzBzu/mAJ6CMolA6M7rLu94l+pkPnBNwgW+yk5ppx9sydcNKhJtwEzqTZ6+WH6ClDDZw6DWhE/YWCOB4dR2OU/1DC/dIwhzzmTtVTO86NDlhLNJ1SYH/JTFuwX6ptMHSKBN3oRJ1f+o4laZEef33cOakmVmBb+fQ3ohwJchBwatVZwapcEPlFi7QYc9/A7PCIs8/E4VGn61YczOf3UNW080O91Ah03bXt1DEq8orFRORbs2FHR8tZfD2vZKkEN5tMkU3UzoHmdcnCaTrYxw7ctgrKVAFX68', 'jj/edGR3q9lWcUYry+wW8fr5Yyii5XYiTHTlUfRNKh2TZT2Il5ywg/G2IJ2W4/0AXF/Uo/iZADW5IAzDKoMVnFBMdHghUPb4JQjOHifc0wo8Y4DAUHqr+esPz1BJNxxv5/KsVTruAPlXDldBPYWGcUbfA7iBb9whkxWh6BBtl2tBx2qmylr3mpkIODWO7OYBK5pFtU2tsYH19esTN2vFlNADjglKUycyzwWEz9COHj2ek0XA/lh/Ft2SFJioXZNckfIgHaZvhFRwgOqZnk7rhSY1XwgLJq3z0nFqlTFlHhnJSjuRfSTDOWPOV7eKQRie7gSRLH30DwXgImHmA+vCvGeQVEQJjZoSKK/Vjc+Jp1LQ4IZ+DXk/9ZIojgAv+UG1DqVckKzXmLYwGtfAsq7bPF565Q9+Bp6tGj4cHGrvqih1SPJDqAlnxRNVXI0jdK9m1cnz8IUoG/eF1xnJS4zYvOmr0c9EImRftSrgCsxMcfPpxFkHlnRm5apoTuqOter1puZ48aOXRPRVs4K+r0rc9TR8mQt/rHU4r8KRjAjYklsbCvgCkjmRRGv0WUcTPfTU2mRR4fqEyFi70m+JwPGnkpybN/rQttn4eH9K+bDAKkcFQjm9EyhyaMjk4+NShUJVKCItI0+2jqOlx8GT3eayibttSYRgo9Pd/B1QTZxduj9PNP8nt6u6RbCggw2pVLi+tueSuOWwEo6s09xzVkBTTdZHVGMcAiq9xiHHVYAM3uq+gqvdvlugSjR6qBShzYOMK+/7I8So8fuyHBBMy2oBB0sMo/x4Yg5WIThaEfk+aqX/mVsxRzUVq+dkr+MhMklZ4mWZ3IhCXSJssqJVIsjUXowwBe', '=kHpIdPU2OKWLTSx7hmRK0z34QlHc4vImHAyz/Dw4+SM/NpAu9T84bhm4Xpj+svsTCVj4YbTFEh/RgaFN8Mipo0whKmr0pLQ2Lc2t4pGt92ybiGDXIa0oz1G67usiLgF9MWJPsT6JqCxZRf2YZvORp8r/M0mAVdDRmxtZo61gulDJS48THf78dZ+QkuHU4U0bBP+35P7ZYDEkX5qJ1+J8WNEFTrDG2hoFkST66BtrSWE+UIZ4/NQTOyV8wUjcvPujUmBIkKt70vKK22RkzyWuTxp4X8WQaGQ3hZKklzIlRmQdWrar3uQmqS6FPLzo1C1GVeDpWLlDNfgd6Ub/1xEW93PaYRoylh2G1VaR2+9TwAAI5uI/W/QcHd4cYFG9xRTI0qcoIh8pvsqgjZJe8oIf0aQMGTJDmrnw9g+hfpDHsAIjC2xt99C8c4C/E8Hqxd3N02qbSAzP6riMvxeSASY30Y/tHIZfF3g0eGLzOQ9B+wpIRLTTZPzDMkZ8bHQxZGAU9h5Uk5HMxoxDqCS9QV7HvPUme6g6EC5kq43x3H+6oTh+xDH7aBW0mjOpQqN0OvQo06b+RVbe+coPGngjr/1Ugy3o61Zv/lzMrskRDftqI2VSu8caIIHpLSl5a/PtVOK8szGZXUfNDrORCVyqKKhco0rqZTEeiF2f0Q9twaEF1iq/vk6jbHrrmcE3A5tpGYX+9SqGXMtRJrxE6oBJNVHyoK7Y/GqzwB6uAFJ9aMW+4l4xnmQo1dyhiEx7kayY+dwfMngkAYupOGOQo68aaAu2pAEY8VOsCW6AjMzNsuaFL4UCAN46JTHxsGYgTi7fHvXUIC54ppFsL/gA04abskq9m/PVEb8MJ']

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
