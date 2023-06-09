import sys

readl = sys.stdin.readline
n = int(readl())
answer = 1

for i in range(2, n+1):
    if i % 2 == 0:
        answer = (answer * 2) + 1
    else:
        answer = (answer * 2) - 1


print(answer % 10_007)

