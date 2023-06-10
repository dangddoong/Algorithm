import sys
readl = sys.stdin.readline

t = int(readl())
sum_cases = [1, 2, 4]

for _ in range(t):
    n = int(readl())
    if len(sum_cases) >= n:
        print(sum_cases[n-1])
    else:
        for i in range(len(sum_cases), n):
            case = sum_cases[i-3] + sum_cases[i-2] + sum_cases[i-1]
            sum_cases.append(case)
        print(sum_cases[n-1])

