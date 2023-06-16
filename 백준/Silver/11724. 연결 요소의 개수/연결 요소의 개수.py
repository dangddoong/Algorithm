import sys
from collections import deque

readl = sys.stdin.readline
n, m = map(int, readl().split())
visited = [False] * (n+1)
connected = {}
for i in range(1, n+1):
    connected[i] = []

for asdf in range(m):
    a, b = map(int, readl().split())
    connected[a].append(b)
    connected[b].append(a)

count = 0
deq = deque()
while connected:
    if not deq:
        count += 1
        num, li = connected.popitem()
        visited[num] = True
        for n in li:
            if not visited[n]:
                deq.append(n)
                visited[n] = True

    for _ in range(len(deq)):
        num = deq.popleft()
        li = connected[num]
        del connected[num]
        for n in li:
            if not visited[n]:
                deq.append(n)
                visited[n] = True

print(count)
