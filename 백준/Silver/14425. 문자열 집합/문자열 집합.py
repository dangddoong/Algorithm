import sys

readl = sys.stdin.readline
n, m = map(int, readl().split())
keywordMap = {}
count = 0
for _ in range(n):
    keywordMap[readl().rstrip()] = 0

for _ in range(m):
    if readl().rstrip() in keywordMap:
        count += 1
print(count)