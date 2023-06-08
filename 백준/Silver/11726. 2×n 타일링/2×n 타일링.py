# 코드 리팩토링
import sys
readl = sys.stdin.readline

n = int(readl())

dp = [1, 2]
if n > 2:
    for i in range(2, n):
        dp.append(dp[i-2] + dp[i-1])

print(dp[n-1] % 10_007)


# import sys
# readl = sys.stdin.readline

# n = int(readl())
# if n == 1:
#     print(1)
#     exit(0)
# if n == 2:
#     print(2)
#     exit(0)

# dp = [1, 2]
# for i in range(2, n):
#     dp.append(dp[i-2] + dp[i-1])

# print(dp[n-1] % 10_007)
