import sys
readl = sys.stdin.readline

n = int(readl())

array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append([y, x])

s_array = sorted(array)

for y, x in s_array:
    print(x, y)
