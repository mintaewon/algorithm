import sys
input = sys.stdin.readline

N = int(input())
answer = [1] *N
ls = []
for i in range(N):
    ls.append(tuple(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if (ls[j][0] < ls[i][0]) and (ls[j][1] < ls[i][1]):
            answer[j] += 1
print(*answer)