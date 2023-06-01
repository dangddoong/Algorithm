import sys
from collections import deque
readl = sys.stdin.readline
n, m, v = map(int, readl().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]
visited_dfs, visited_bfs = [False] * (n+1), [False] * (n+1)
answer_dfs, answer_bfs = [], []

for _ in range(m):
    a, b = map(int, readl().split())
    graph[a][b] = True
    graph[b][a] = True


def dfs(now):
    visited_dfs[now] = True
    answer_dfs.append(str(now))
    for i in range(1, n+1):
        if not visited_dfs[i] and graph[now][i]:
            dfs(i)


def bfs(now):
    queue = deque([now])
    visited_bfs[now] = True
    while queue:
        now = queue.popleft()
        answer_bfs.append(str(now))
        for j in range(1, n+1):
            if not visited_bfs[j] and graph[now][j]:
                queue.append(j)
                visited_bfs[j] = True


dfs(v)
print(' '.join(answer_dfs))
bfs(v)
print(' '.join(answer_bfs))

