import sys

readl = sys.stdin.readline
n = int(readl())
li = []
answer = []

for _ in range(n):
    x, y = map(int, readl().split())
    li.append([x, y])

for me in li:
    rank = 1
    for other in li:
        if other[0] > me[0] and other[1] > me[1]:
            rank += 1
    answer.append(str(rank))

print(" ".join(answer))
