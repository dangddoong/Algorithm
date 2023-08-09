import sys

readl = sys.stdin.readline
n = int(readl())

for i in range(max(1, n - (len(str(n) * 9))), n):
    hab = i
    str_i = str(i)
    for num in str_i:
        hab += int(num)
    if hab == n:
        print(i)
        exit()

print(0)
