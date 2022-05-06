import sys
input = sys.stdin.readline

N = int(input())
ls = set()
for _ in range(N):
    ls.add(int(input()))

for i in sorted(ls):
    print(i)