import sys
readl = sys.stdin.readline
s = readl().rstrip()

s = s.replace("XXXX", "AAAA")
s = s.replace("XX", "BB")
if "X" in s:
    print(-1)
else:
    print(s)
