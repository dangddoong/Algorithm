import sys

readl = sys.stdin.readline
n = int(readl())
set_a = set(map(int, readl().split()))
m = int(readl())
li_b = list(map(int, readl().split()))

for num in li_b:
    if num in set_a:
        print(1)
    else:
        print(0)
