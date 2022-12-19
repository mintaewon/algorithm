def func(x, l, r, c):
    if l>=r:
        return 1, c
    elif x[l] !=x[r]:
        return 0, c
    else:
        return func(x, l+1, r-1, c+1)
    
n=int(input())
for i in range(n):
    s = input()
    l,r = 0, len(s)-1
    cnt = 1
    print(*func(s,l,r, cnt))