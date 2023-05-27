import sys
readl = sys.stdin.readline
n = int(readl())
word = [readl().rstrip() for _ in range(n)]


for w in word:
    if w[::-1] in word:
        print(str(len(w)) + " " + w[len(w)//2])
        break

