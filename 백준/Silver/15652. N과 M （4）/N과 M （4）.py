import sys

readl = sys.stdin.readline
n, m = map(int, readl().split())
s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if len(s) != 0 and s[-1] > i:
            continue
        s.append(i)
        dfs()
        s.pop()


dfs()
