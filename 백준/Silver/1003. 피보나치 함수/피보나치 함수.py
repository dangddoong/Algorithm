import sys

readl = sys.stdin.readline
t = int(readl())
fibonacci = {"0": [1, 0], "1": [0, 1]}


def fibo(n):
    if str(n) in fibonacci:
        return fibonacci[str(n)]
    else:
        fibonacci[str(n)] \
            = [fibo(n-1)[0]+fibo(n-2)[0], fibo(n-1)[1]+fibo(n-2)[1]]
        return fibonacci[str(n)]


for _ in range(t):
    answer = fibo(int(readl()))
    print(*answer)
