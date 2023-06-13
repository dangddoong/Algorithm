import sys
from collections import deque

readl = sys.stdin.readline
t = int(readl())

for _ in range(t):
    a, b = map(int, readl().split())
    deq = deque()
    deq.append((a, ""))
    visited = [False] * 10000

    while deq:
        num, order = deq.popleft()

        if num == b:
            print(order)
            break

        # 1
        num2 = (2 * num) % 10000
        if not visited[num2]:
            deq.append((num2, order + "D"))
            visited[num2] = True
        # 2
        num2 = (num - 1) % 10000
        if not visited[num2]:
            deq.append((num2, order + "S"))
            visited[num2] = True
        # 3
        num2 = (10 * num + (num // 1000)) % 10000
        if not visited[num2]:
            deq.append((num2, order + "L"))
            visited[num2] = True

        # 4
        num2 = (num // 10 + (num % 10) * 1000) % 10000
        if not visited[num2]:
            deq.append((num2, order + "R"))
            visited[num2] = True
