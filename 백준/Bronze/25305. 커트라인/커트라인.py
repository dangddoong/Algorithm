import sys
readl = sys.stdin.readline

n,k = [int(i) for i in readl().split()]
scores = [int(i) for i in readl().split()]

scores.sort()
print(scores[-k])