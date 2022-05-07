import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
ls = []
for _ in range(N):
    ls.append(int(input()))
ls = sorted(ls, reverse=True)

# 평균
print(int(round(sum(ls) / N, 0)))
# 중앙값
print(ls[len(ls)//2])
# 최빈값
cnt_ls = sorted(Counter(ls).items(), key=lambda x: (-x[1], x[0]))
if len(cnt_ls) > 1:
    if cnt_ls[0][1] == cnt_ls[1][1]:
        print(cnt_ls[1][0])
    else:
        print(cnt_ls[0][0])
else:
    print(cnt_ls[0][0])
# 최대 최소 차이
print(abs(ls[0] - ls[-1]))