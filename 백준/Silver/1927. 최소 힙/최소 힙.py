import heapq
import sys

readl = sys.stdin.readline
n = int(readl())
heap = []

for _ in range(n):
    x = int(readl())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)
        