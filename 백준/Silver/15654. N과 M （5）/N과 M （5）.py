import sys

readl = sys.stdin.readline
n, m = map(int, readl().split())
nums = sorted(list(map(int, readl().split())))
s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for num in nums:
        if len(s) != 0 and num in s:
            continue
        s.append(num)
        dfs()
        s.pop()


dfs()
