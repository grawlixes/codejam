from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(2000)

from bisect import bisect_left, bisect_right
from collections import deque
from functools import lru_cache, reduce
from heapq import heappush, heappop
from math import sqrt, ceil, floor, log2

T = int(input())

def rl(t = int):
    return list(map(t, input().split()))

def ans(t, s):
    print("Case #%i: %s" % (t, s))


# [10, 30, 40] -> 40, 40
# [20, 50, 60] -> 60, 100
# [50, 60, 60] -> 50, 110
for t in range(1, T + 1):
    n, p = rl()
    c = []
    for _ in range(n):
        c.append(rl())
        c[-1].sort()

    @lru_cache(None)
    def dfs(i = 0, last = 0):
        if i == n:
            return 0
        
        lo, hi = c[i][0], c[i][-1]
    
        ret = float('inf')
        if last <= lo:
            ret = dfs(i + 1, hi) + (hi - last)
        elif lo < last and last < hi:
            endLo = dfs(i + 1, lo) + (hi - last) + (hi - lo)
            endHi = dfs(i + 1, hi) + (last - lo) + (hi - lo)

            ret = min(endLo, endHi)
        else:
            ret = dfs(i + 1, lo) + (last - lo)

        return ret

    ans(t, str(dfs()))
