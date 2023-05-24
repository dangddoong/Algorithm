import sys
readl = sys.stdin.readline
n = int(readl())
nums = [int(i) for i in readl().split()]
count = 0

for i in range(n):
    err = 0
    if nums[i] == 1: 
        continue
    if nums[i] == 2:
        count += 1
        continue
    for j in range(2, nums[i]):
        if nums[i] % j == 0:
            err += 1
            break
    if err == 0:
        count += 1
print(count)

