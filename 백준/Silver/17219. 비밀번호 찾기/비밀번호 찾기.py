import sys
readl = sys.stdin.readline

n, m = map(int, readl().split())
memo = {}

for _ in range(n):
    site, password = readl().split()
    memo[site] = password

for _ in range(m):
    site = readl().rstrip()
    sys.stdout.write(memo[site] + "\n")