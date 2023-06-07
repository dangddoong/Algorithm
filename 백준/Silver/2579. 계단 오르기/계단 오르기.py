import sys
readl = sys.stdin.readline

stairs = int(readl())
points = [0 for _ in range(stairs)]
dp = points.copy()
for i in range(stairs):
    points[i] = int(readl())

if stairs == 1:
    print(points[0])
    exit()
elif stairs == 2:
    print(points[0]+points[1])
    exit()

dp[0], dp[1] = points[0], points[0]+points[1]
dp[2] = max(points[0], points[1]) + points[2]

for i in range(3, stairs):
    dp[i] = max(dp[i-2], dp[i-3]+points[i-1]) + points[i]

print(dp[stairs-1])
