import sys

readl = sys.stdin.readline
n = int(readl())
factorial = n

for num in range(2, n):
    factorial *= num

factorial = str(factorial)
idx = -1

for _ in range(len(factorial)):
    if factorial[idx] != '0':
        print((idx * -1) - 1)
        exit(0)
    idx -= 1
print(0)