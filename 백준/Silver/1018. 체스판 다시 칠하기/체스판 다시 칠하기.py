import sys
readl = sys.stdin.readline
n, m = map(int, readl().split())
rows = [readl() for _ in range(n)]
answer = []

for i in range(n-7):
    for j in range(m-7):
        first_w, first_b = 0, 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if rows[a][b] == "W":
                        first_b += 1
                    else:
                        first_w += 1
                else:
                    if rows[a][b] == "W":
                        first_w += 1
                    else:
                        first_b += 1
        answer.append(first_b)
        answer.append(first_w)
print(min(answer))
