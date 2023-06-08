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

# 위는 dict&재귀 기반 TopDown 방식
# 아래는 list기반 BottomUp 방식

# import sys

# readl = sys.stdin.readline
# t = int(readl())
# zero_fibo, one_fibo = [1, 0], [0, 1]

# for _ in range(t):
#     n = int(readl())
#     len_zero = len(zero_fibo)
#     if len_zero <= n:
#         for i in range(len_zero, n + 1):
#             zero_fibo.append(zero_fibo[i-1] + zero_fibo[i-2])
#             one_fibo.append(one_fibo[i-1] + one_fibo[i-2])

#     answer = [zero_fibo[n], one_fibo[n]]
#     print(*answer)
