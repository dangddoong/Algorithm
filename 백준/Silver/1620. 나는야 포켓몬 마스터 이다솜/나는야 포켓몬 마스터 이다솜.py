import sys

readl = sys.stdin.readline
n, m = map(int, readl().split())
byNum = []
byName = {}
ord_A, ord_Z = ord('A'), ord('Z')

for i in range(1, n+1):
    name = readl().rstrip()
    byNum.append(name)
    byName[name] = i

for _ in range(m):
    order = readl().rstrip()
    if ord_A <= ord(order[0]) <= ord_Z:
        print(byName[order])
    else:
        print(byNum[int(order) - 1])

