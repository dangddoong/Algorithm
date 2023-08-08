import sys

readl = sys.stdin.readline

r_list = [31**i for i in range(int(readl()))]
s = readl().rstrip()
answer = 0

for i in range(len(s)):
    answer += (ord(s[i]) - ord('a') + 1) * r_list[i]

print(answer)