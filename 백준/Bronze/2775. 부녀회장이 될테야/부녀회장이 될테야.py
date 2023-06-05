# DP
import sys
readl = sys.stdin.readline

test_case = int(readl())
for _ in range(test_case):
    k = int(readl())
    n = int(readl())
    apart = [[0 for _ in range(n)] for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n):
            if i == 0:
                apart[i][j] = j + 1
            elif j == 0:
                apart[i][j] = 1
            else:
                apart[i][j] = apart[i-1][j] + apart[i][j-1]
    print(apart[k][n-1])