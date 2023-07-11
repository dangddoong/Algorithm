import sys

readl = sys.stdin.readline
N, M = map(int, readl().split())
numbers = list(map(int, readl().split()))
answer = 0

for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            if i == j or i == k or j == k:
                continue

            s = numbers[i] + numbers[j] + numbers[k]
            if answer < s <= M:
                answer = s

print(answer)