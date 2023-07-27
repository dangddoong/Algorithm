import sys

readl = sys.stdin.readline
n = int(readl())
li_a = list(map(int, readl().split()))
m = int(readl())
li_b = list(map(int, readl().split()))

dictionary = {}
for num in li_a:
    dictionary[num] = 0
for num in li_b:
    if num in dictionary:
        print(1)
    else:
        print(0)
