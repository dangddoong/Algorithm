import sys

readl = sys.stdin.readline
n = int(readl())

if n < 100:
    print(n)
    exit(0)

cnt = 99
for num in range(111, n+1):
    li = list(map(int, str(num)))
    if li[2] - li[1] == li[1] - li[0] or li[1] - li[2] == li[0] - li[1]:
        cnt += 1
print(cnt)
