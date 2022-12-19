n=int(input())
ls = list(map(int, input().split()))

sort_ls = sorted(list(set(ls)))
dic = {}
for i in range(len(sort_ls)):
    dic[sort_ls[i]] = i

for i in ls:
    print(dic[i], end=" ")