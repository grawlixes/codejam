from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10000)
T = int(input())

@lru_cache(None)
def dfs(s, x, y, i, prev):
    if i == len(s):
        return 0
    elif s[i] == '?':
        addJ = 0 if prev != 'C' else x
        addC = 0 if prev != 'J' else y

        return min(dfs(s, x, y, i + 1, 'C') + addC, \
                   dfs(s, x, y, i + 1, 'J') + addJ)
    else:
        add = 0
        if prev == 'C' and s[i] == 'J':
            add = x
        elif prev == 'J' and s[i] == 'C':
            add = y
        else:
            pass

        return dfs(s, x, y, i + 1, s[i]) + add

for t in range(1, T + 1):
    arg = input().strip().split()
    x, y, s = int(arg[0]), int(arg[1]), arg[2]

    print("Case #" + str(t) + ": " + str(dfs(s, x, y, 0, None))) 
