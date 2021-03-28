# this only passes the first two tests,
# need sub-logarithmic complexity for 3

T, n, q = map(int, input().split())

#f = open("out.txt", 'w')
for t in range(1, T + 1):
    print(1, 2, 3)
    ret = [int(input())]
    others = set([1,2,3]) - set(ret)
    ret = [others.pop()] + ret + [others.pop()]
   
    for i in range(4, n + 1):
        #f.write(str(ret) + '\n')
        l, r = 0, len(ret) - 1
        while l != r:
            m = (l + r) // 2
            #f.write(str((l, m, r)) + '\n')
            left, right = ret[m], ret[r]
            print(left, i, right)
            ans = int(input())

            if ans == left:
                r = m
            elif ans == right:
                l = r = r + 1
            else:
                l = m + 1

        ret.insert(l, i)
    
    print(' '.join(str(el) for el in ret))
    if int(input()) != 1:
        exit()
