import sys

readl = sys.stdin.readline

t = int(readl())
P = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(t):
    n = int(readl())
    if len(P) >= n:
        print(P[n - 1])
    else:
        for i in range(len(P), n):
            case = P[i-1] + P[i-5]
            P.append(case)
        print(P[n - 1])
