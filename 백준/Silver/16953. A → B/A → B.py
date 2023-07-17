import sys

readl = sys.stdin.readline
a, b = map(int, readl().split())
count = -1


def cal(now, target, depth):
    global count
    if now == target:
        if count == -1 or count > depth:
            count = depth
        return
    if now > target:
        return

    cal(now*2, target, depth+1)
    cal(int(str(now) + '1'), target, depth+1)


cal(a, b, 0)
if count == -1:
    print(-1)
else:
    print(count+1)
