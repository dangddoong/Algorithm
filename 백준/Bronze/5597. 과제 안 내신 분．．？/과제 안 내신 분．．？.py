import sys
readl = sys.stdin.readline

answer = list(range(1, 31))
for _ in range(28):
    n = int(readl().rstrip())
    answer.remove(n)
print(answer[0])
print(answer[1])