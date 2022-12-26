import re
import math
import numpy as np
from functools import lru_cache

with open('./in/19.txt') as f:
    bps = [tuple(map(int, re.findall(r'\d+', line))) for line in f.read().strip().splitlines()]

I = np.identity(4, dtype=int)

qualities = []
bests = []
for i, Aa, Ba, Ca, Cb, Da, Dc in bps:
    LA = max((Ba, Ca, Da))
    La = max(Aa, LA)
    LB = Lb = Cb
    LC = Lc = Dc
    @lru_cache(maxsize=None)
    def max_geodes(a, b, c, d, A, B, C, D, t):
        if t == 0:
            return d
        if a > La * (t - 1) or b > Lb * (t - 1) or c > Lc * (t - 1):
            return max_geodes(min(a, La * (t - 1)), min(b, Lb * (t - 1)), min(c, Lc * (t - 1)), d, A, B, C, D, t)
        best = max_geodes(a + A, b + B, c + C, d + D, A, B, C, D, t - 1)
        if A < LA and Aa <= a:
            best = max(best, max_geodes(a - Aa + A, b + B, c + C, d + D, A + 1, B, C, D, t - 1))
        if B < LB and Ba <= a:
            best = max(best, max_geodes(a - Ba + A, b + B, c + C, d + D, A, B + 1, C, D, t - 1))
        if C < LC and Ca <= a and Cb <= b:
            best = max(best, max_geodes(a - Ca + A, b - Cb + B, c + C, d + D, A, B, C + 1, D, t - 1))
        if Da <= a and Dc <= c:
            best = max(best, max_geodes(a - Da + A, b + B, c - Dc + C, d + D, A, B, C, D + 1, t - 1))
        return best
    geodes = max_geodes(0, 0, 0, 0, 1, 0, 0, 0, 24)
    qualities.append(i * geodes)
    if i <= 3:
        geodes = max_geodes(0, 0, 0, 0, 1, 0, 0, 0, 32)
        bests.append(geodes)
    max_geodes.cache_clear()

print(sum(qualities))
print(math.prod(bests))
