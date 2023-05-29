import sys
readl = sys.stdin.readline

while True:
    n = readl().rstrip()
    if int(n) == 0:
        break
    if n == n[::-1]:
        print("yes")
    else:
        print("no")