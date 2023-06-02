import sys
n = int(sys.stdin.readline())
memo = [0] * (n + 1)

for i in range(2, n+1):
    if i % 2 == 0 and i % 3 == 0:
        memo[i] = min(memo[i//3], memo[i//2]) + 1
    elif i % 2 == 0:
        memo[i] = min(memo[i//2], memo[i-1]) + 1
    elif i % 3 == 0:
        memo[i] = min(memo[i//3], memo[i-1]) + 1
    else:
        memo[i] = memo[i-1] + 1

print(memo[n])
