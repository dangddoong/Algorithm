import sys

readl = sys.stdin.readline
n = int(readl())
dp = [0,1,2,3,5,8]
if n <= 5:
    print(dp[n])
    exit(0)

for i in range(6, n+1):
    dp.append((dp[-2] + dp[-1]) % 15746)

print(dp[n])

