import sys

readl = sys.stdin.readline
t = int(readl())

for i in range(t):
    n = int(readl())
    weardict = {}
    for j in range(n):
        wear = list(readl().split())
        if wear[1] in weardict:
            weardict[wear[1]].append(wear[0])
        else:
            weardict[wear[1]] = [wear[0]]

    cnt = 1 # 각 종류마다 항목의 개수

    for k in weardict:
        cnt *= (len(weardict[k])+1)
    print(cnt-1)