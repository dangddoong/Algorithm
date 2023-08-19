import sys
readl = sys.stdin.readline

n = int(readl())

array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append(y * 1_000_000 + x + 100_000)

array.sort()
for num in array:
    print((num % 1_000_000) - 100_000, num//1_000_000)
