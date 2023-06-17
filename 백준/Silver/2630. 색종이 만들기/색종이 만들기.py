import sys

readl = sys.stdin.readline
n = int(readl())
paper = [readl().split() for _ in range(n)]
zero_block, one_block = 0, 0


def conquest(x, y, length):
    global zero_block, one_block
    if length > 1:
        half_length = length//2
        for a in range(x, x+length):
            for b in range(y, y+length):
                if paper[y][x] != paper[b][a]:
                    conquest(x, y, half_length)
                    conquest(x, y+half_length, half_length)
                    conquest(x+half_length, y, half_length)
                    conquest(x+half_length, y+half_length, half_length)
                    return
    if paper[y][x] == "0":
        zero_block += 1
    else:
        one_block += 1


conquest(0, 0, n)
print(zero_block)
print(one_block)
