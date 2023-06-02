import sys
readl = sys.stdin.readline
n, s = map(int, readl().split())
nums = [int(i) for i in readl().split()]
count = 0


def tracking(depth, index, sum):
    global count
    if sum == s and depth != 0:
        count += 1
    if depth == n or index > n:
        return
    for i in range(index, n):
        sum_copy = sum
        sum_copy += nums[i]
        tracking(depth+1, i+1, sum_copy)


tracking(0, 0, 0)
print(count)