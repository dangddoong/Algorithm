import sys
readl = sys.stdin.readline
n = int(readl())

for i in range(1, n+1):
    word = readl().split()
    case = "Case #" + str(i) + ":"
    for i in range(len(word)):
        case += " " + word.pop()
    print(case)