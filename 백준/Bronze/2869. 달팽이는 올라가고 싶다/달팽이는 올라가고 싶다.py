import sys

readl = sys.stdin.readline
a,b,v = map(int, readl().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)
