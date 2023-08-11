import sys


def my_round(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


readl = sys.stdin.readline
n = int(readl())
cut = my_round(n * 0.15)
if n == 0:
    print(0)
    exit(0)

difficulties = [int(readl()) for _ in range(n)]
difficulties.sort()
difficulties = difficulties[cut:-cut] if cut else difficulties
print(my_round(sum(difficulties) / (n - cut * 2)))
