# This only solves the first set,
# but I think I'm close for the second.

T = int(input())
P = int(input())

from math import e

def f(s, q):
    return 1 / (1 + math.e**(q - s))
    
for t in range(1, T + 1):
    res = [input().strip() for _ in range(100)]
    diff = [1 - sum(int(res[i][j]) for i in range(100)) / 100 \
            for j in range(10000)]
    
    sus = [(sum(diff[j]*int(res[i][j]) for j in range(10000)), i+1)\
            for i in range(100)]

    sus.sort(reverse = True)

    print("Case #" + str(t) + ": " + str(sus[0][1]))
