import sys

readl = sys.stdin.readline
n = int(readl())
paper = [readl().split() for _ in range(n)]
zero_block, one_block = 0, 0


def conquest(x, y, length):
    global zero_block, one_block
    for a in range(x, x+length):
        for b in range(y, y+length):
            if paper[y][x] != paper[b][a]:
                conquest(x, y, length//2)
                conquest(x, y+length//2, length//2)
                conquest(x+length//2, y, length//2)
                conquest(x+length//2, y+length//2, length//2)
                return
    if paper[y][x] == "0":
        zero_block += 1
    else:
        one_block += 1


conquest(0, 0, n)
print(zero_block)
print(one_block)
