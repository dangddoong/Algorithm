import sys

readl = sys.stdin.readline
n = int(readl())
list_a = sorted(list(map(int, readl().split())), reverse=True)
list_b = sorted(list(map(int, readl().split())))

answer = 0
for i in range(n):
    answer += list_a[i] * list_b[i]

print(answer)

