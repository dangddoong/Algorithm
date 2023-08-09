import sys

readl = sys.stdin.readline
n = int(readl())

for i in range(1, n):
    hab = i
    str_i = str(i)
    for j in range(len(str_i)):
        hab += int(str_i[j])
    if hab == n:
        print(i)
        exit()

print(0)
