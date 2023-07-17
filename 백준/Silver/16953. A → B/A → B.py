import sys
from collections import deque

readl = sys.stdin.readline
a, b = map(int, readl().split())
depth = 1
deq = deque([a*2, int(str(a) + '1')])

while deq:
    length = len(deq)
    for _ in range(length):
        now = deq.popleft()
        if now == b:
            print(depth+1)
            exit(0)
        elif now > b:
            continue
        deq.append(now*2)
        deq.append(int(str(now) + '1'))
    depth += 1

print(-1)
