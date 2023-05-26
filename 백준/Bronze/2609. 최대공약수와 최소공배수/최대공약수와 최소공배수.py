import sys
readl = sys.stdin.readline
n, m = readl().split()
n, m = int(n), int(m)

min, max, num = 0, 0, 1
while True:
    if n % num == 0 and m % num == 0:
        max = num
    if num % n == 0 and num % m == 0:
        min = num
        break
    num += 1
print(str(max) + "\n" + str(min))