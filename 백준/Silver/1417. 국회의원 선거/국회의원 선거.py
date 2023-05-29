import sys

readl = sys.stdin.readline
n = int(readl())
dasom = int(readl())
others = [int(readl()) for _ in range(n - 1)]
answer = 0

if n == 1:
    print(0)
    exit(0)
    
while True:
    others.sort()
    if others[-1] >= dasom:
        others[-1] -= 1
        dasom += 1
        answer += 1
    else:
        print(answer)
        break
