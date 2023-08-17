import sys

readl = sys.stdin.readline
n = int(readl())
answer = 0

while n >= 0:
    if n % 5 == 0:
        answer += (n // 5)
        print(answer)
        exit(0)
    n -= 3
    answer += 1
    
print(-1)
