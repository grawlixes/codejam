import sys
input = sys.stdin.readline

from bisect import bisect_left, bisect_right
from collections import deque
from functools import lru_cache, reduce
from heapq import heappush, heappop
from math import sqrt, ceil, floor, log2
from random import randint

T = int(input())

def rl(t = int):
    return list(map(t, input().split()))

def ans(t, s):
    print("Case #%i: %s" % (t, s))

def p(s):
    print(s)
    sys.stdout.flush()

m = []
for numBits in range(4 + 1):
    bits = [n for n in range(1 << 8) if sum((n >> i) & 1 for i in range(8)) == numBits]
    m.append(bits)

MASK = (1 << 8) - 1

for t in range(1, T + 1):
    s = "00000000"
    p(s)
    # n will be the number of bits set
    n = int(input())
    bi = 0
    while n not in [0, -1, 8]:
        bind = n if n <= 4 else (8 - n)
        b = m[bind][randint(0, len(m[bind]) - 1)]

        if n > 4:
            b = MASK - b
        
        this = bin(b)[2:]
        while len(this) < 8:
            this = '0' + this
        p(this)
        n = int(input())

    if n == 8:
        p("11111111")
        n = int(input())
    
    if n == -1:
        raise RuntimeError("Your code sucks")
