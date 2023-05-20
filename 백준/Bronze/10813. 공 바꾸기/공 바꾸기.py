import sys
readl = sys.stdin.readline

n,m = [int(i) for i in readl().split()]
rows = [[int(i) for i in readl().split()] for _ in range(m)]
li = [i for i in range(1, n+1)]

for i in range(m):
    mock = li[rows[i][0]-1]
    li[rows[i][0]-1] = li[rows[i][1]-1]
    li[rows[i][1]-1] = mock
print(' '.join(str(n) for n in li))
