import sys

readl = sys.stdin.readline
n = int(readl())
di = {}

for _ in range(n):
    x, y = map(int, readl().split())
    if x in di:
        di[x].append(y)
    else:
        di[x] = [y]

li = sorted(list(di.keys()))

for x in li:
    for y in sorted(di[x]):
        print(*[x, y])

