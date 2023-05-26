import sys
readl = sys.stdin.readline
n = int(readl())
num, cnt = 1, 1

while True:
    if n <= num:
        print(cnt)
        break
    num += 6 * cnt
    cnt += 1