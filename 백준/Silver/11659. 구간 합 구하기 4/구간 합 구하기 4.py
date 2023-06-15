import sys

readl = sys.stdin.readline
n, m = map(int, readl().split())
li = list(map(int, readl().split()))
li_sum = [0]

for num in li:
    li_sum.append(li_sum[-1] + num)

for _ in range(m):
    start, finish = map(int, readl().split())
    answer = li_sum[finish] - li_sum[start-1]
    print(answer)
