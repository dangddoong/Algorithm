import sys
from collections import deque
readl = sys.stdin.readline
n, m, v = map(int, readl().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]
visited_dfs, visited_bfs = [False] * (n+1), [False] * (n+1)

for _ in range(m):
    a, b = map(int, readl().split())
    graph[a][b] = True
    graph[b][a] = True


def dfs(now):
    visited_dfs[now] = True
    print(now, end=" ")
    for i in range(1, n+1):
        if not visited_dfs[i] and graph[now][i]:
            dfs(i)


def bfs(now):
    queue = deque([now])
    visited_bfs[now] = True
    while queue:
        now = queue.popleft()
        print(now, end=" ")
        for j in range(1, n+1):
            if not visited_bfs[j] and graph[now][j]:
                queue.append(j)
                visited_bfs[j] = True


dfs(v)
print()
bfs(v)
