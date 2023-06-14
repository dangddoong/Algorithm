import sys

readl = sys.stdin.readline
n = int(readl())
scores = list(map(int, readl().split()))
answer, max_score = 0, 0

for score in scores:
    answer += score
    if score > max_score:
        max_score = score

answer = (answer/max_score) * 100 / n
print(answer)