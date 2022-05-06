def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

T = int(input())
visited = [0] * (T+1)
graph = [[] for _ in range(T+1)]
for _ in range(int(input())):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(sum(visited)-1)