import sys
from collections import deque

readl = sys.stdin.readline
n, k = map(int, readl().split())
sec = 0
visited = [False]*100_001
deq = deque([n])

if n >= k:
    print(n-k)
    exit(0)

while True:
    for _ in range(len(deq)):
        now = deq.popleft()

        if now == k:
            print(sec)
            exit(0)
        if now-1 >= 0 and not visited[now-1]:
            visited[now-1] = True
            deq.append(now-1)
        if now+1 <= 100_000 and not visited[now+1]:
            visited[now+1] = True
            deq.append(now+1)
        if now*2 <= 100_000 and not visited[now*2]:
            visited[now*2] = True
            deq.append(now*2)
    sec += 1
