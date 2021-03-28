T = int(input())
for t in range(1, T + 1):
    n = int(input())
    l = list(map(int, input().split()))
    ret = 0
    sl = sorted(l)
    
    for i in range(n-1):
        j = i
        while l[j] != sl[i]:
            j += 1
        ret += j - i + 1
        for k in range((j - i + 1) // 2):
            i2, j2 = i + k, j - k
            l[i2], l[j2] = l[j2], l[i2]
            
    print("Case #" + str(t) + ": " + str(ret))
