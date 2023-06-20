import sys
readl = sys.stdin.readline

n = int(readl())
time = [list(map(int, readl().split())) for _ in range(n)]
time.sort(key = lambda x:(x[1], x[0]))

cnt, last = 0, -1
for start, end in time:
  if start >= last:
    cnt += 1
    last = end

print(cnt)
