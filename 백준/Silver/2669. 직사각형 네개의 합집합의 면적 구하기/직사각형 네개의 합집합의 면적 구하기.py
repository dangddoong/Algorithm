import sys

readl = sys.stdin.readline
visited = [[False]*101 for _ in range(101)]
area = 0
for _ in range(4):
    x, y, xx, yy = map(int, readl().split())
    for a in range(x, xx):
        for b in range(y, yy):
            if not visited[b][a]:
                area += 1
                visited[b][a] = True

print(area)