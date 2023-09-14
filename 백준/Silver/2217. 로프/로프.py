import sys

readl = sys.stdin.readline
n = int(readl())
ropes = [int(readl()) for _ in range(n)]
ropes.sort(reverse=True)
maximum_weight = 0

for i in range(n):
    if ropes[-1] * (n - i) > maximum_weight:
        maximum_weight = ropes[-1] * (n - i)
    ropes.pop()

print(maximum_weight)
