import sys
readl = sys.stdin.readline
n = readl().rstrip()
int_n = int(n)
m = int(readl())
min_diff, final_depth = abs(100-int_n), 0
button = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if m != 0:
    broken = map(int, readl().split())
    for i in broken:
        button.remove(i)


def tracking(depth, num):
    global min_diff
    global final_depth
    if depth != 0:
        if depth + abs(int_n - int(num)) < min_diff+final_depth:
            min_diff = abs(int_n - int(num))
            final_depth = depth
    if depth == len(n) + 1:
        return
    for j in button:
        num_copy = num
        num_copy += str(j)
        tracking(depth+1, num_copy)


if m == 10:
    print(min_diff)
else:
    tracking(0, "")
    print(final_depth + min_diff)
