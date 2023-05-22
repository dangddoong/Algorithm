import sys
readl = sys.stdin.readline
n = int(readl())
nums = [int(readl()) for _ in range(n)]
for num in sorted(nums):
    print(num)
    