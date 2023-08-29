import sys
from collections import deque

readl = sys.stdin.readline
n, m = map(int, readl().split())
campus = []
visited = [[0 for _ in range(m)] for _ in range(n)]
deq = deque()
for low in range(n):
    line = list(readl().rstrip())
    if "I" in line:
        deq.append((line.index("I"), low))
    campus.append(line)

answer = 0
while deq:
    x, y = deq.popleft()
    if campus[y][x] == "P":
        answer += 1
    elif campus[y][x] == "X":
        continue
        
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] :
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] :
            visited[ny][nx] = True
            deq.append((nx, ny))

if answer == 0:
    print("TT")
else:
    print(answer)
    