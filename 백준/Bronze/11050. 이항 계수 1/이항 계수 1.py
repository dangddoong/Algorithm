import sys

readl = sys.stdin.readline
n, k = map(int, readl().split())

dp = [[1], [1, 1]]
for i in range(2, n+1):
    for j in range(min(i, k)+1):
        if j == 0:
            dp.append([])
        if j == 0 or i == j:
            dp[i].append(1)
            continue
        dp[i].append(dp[i-1][j-1] + dp[i-1][j])

print(dp[n][k])
