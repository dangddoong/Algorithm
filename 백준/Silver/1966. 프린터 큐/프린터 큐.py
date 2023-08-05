import sys
from collections import deque

readl = sys.stdin.readline

for _ in range(int(readl())):
    n, m = map(int, readl().split())
    deq = deque([(idx, i) for idx, i in enumerate(map(int, readl().split()))])
    ranking = 1
    while deq:
        if deq[0][1] < max(deq, key=lambda x: x[1])[1]:
            deq.append(deq.popleft())
            continue
        if deq[0][0] == m:
            print(ranking)
            break
        deq.popleft()
        ranking += 1
