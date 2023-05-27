import sys
readl = sys.stdin.readline
n = int(readl())
bars = [int(readl()) for _ in range(n)]

high = bars.pop()
cnt = 1

for _ in range(len(bars)):
    next = bars.pop()
    if next > high:
        high = next
        cnt += 1

print(cnt)