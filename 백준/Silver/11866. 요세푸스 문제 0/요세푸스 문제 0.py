import sys
from collections import deque

readl = sys.stdin.readline
n, k = map(int, readl().split())
deq = deque([str(i) for i in range(1, n+1)])
answer = []

while deq:
    for _ in range(k-1):
        deq.append(deq.popleft())
    answer.append(deq.popleft())

print('<' + ', '.join(answer) + '>')
