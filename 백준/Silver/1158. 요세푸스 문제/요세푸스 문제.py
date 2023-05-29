import sys
readl = sys.stdin.readline
n, k = readl().split()
n, k = int(n), int(k)
nums = list(range(1, n + 1))
index = k - 1
answer = []
while True:
    len_nums = len(nums)
    if len(answer) == n:
        break
    if index >= len_nums:
        index = index % len_nums
    answer.append(str(nums.pop(index)))
    index += (k - 1)
print("<" + ', '.join(answer) + ">")
