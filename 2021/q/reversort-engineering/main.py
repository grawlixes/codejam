T = int(input())
for t in range(1, T + 1):
    n, c = map(int, input().split())
    ret = []
    if c < n - 1 or c >= (n * (n + 1)) // 2:
        pass
    else:
        i = n
        flip = [0 for _ in range(n+1)]
        tmp = c
        while i > 1:
            left = i - 2
            if tmp >= i + left:
                flip[i] = 1
                tmp -= i 
            else:
                tmp -= 1
            i -= 1

        ret = [0 for _ in range(n)]
        lr = [0, n - 1]
        fi = -1
        ind = 0
        for i in range(1, n + 1):
            if flip[fi]:
                ind = 1 - ind
            ret[lr[ind]] = i
            lr[ind] = (lr[ind] + 1) if ind == 0 else (lr[ind] - 1)
            fi -= 1

    s = "Case #" + str(t) + ": "
    print(s + ("IMPOSSIBLE" if ret == [] else ' '.join(str(el) for el in ret))) 
