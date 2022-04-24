from sys import stdin, setrecursionlimit
input = stdin.readline

from bisect import bisect_left, bisect_right
from collections import deque
from functools import lru_cache, reduce
from heapq import heappush, heappop
from math import sqrt, ceil, floor, log2

T = int(input())

def rl(t = int):
    return deque(map(t, input().split()))

def ans(t, s):
    print("Case #%i: %s" % (t, s))

for t in range(1, T + 1):
    n = int(input())
    a = rl()

    ret = 0
    last = -float('inf')
    while a:
        cur = None
        if a[0] < a[-1]:
            cur = a.popleft()
        else:
            cur = a.pop()

        if cur >= last:
            ret += 1
        last = max(last, cur)

    ans(t, ret)
