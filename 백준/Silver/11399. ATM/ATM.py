import sys
readl = sys.stdin.readline

n = int(readl())
p = list(map(int, readl().split()))
index, answer = 0, 0

p.sort()

for i in range(n, 0, -1):
    answer += p[index] * i
    index += 1

print(answer)
