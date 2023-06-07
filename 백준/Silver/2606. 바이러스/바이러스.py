# dict 활용하여 간선 양방향으로 연결해두고
# visited 활용하여 방문여부 체크
# 1번부터 재귀로 물고가면서 컴퓨터 수 체크

import sys
readl = sys.stdin.readline

computer = int(readl())
ganseon = {}
visited = [False for _ in range(computer + 1)]
visited[1] = True
count = 0


for _ in range(int(readl())):
    a, b = readl().split()
    if a in ganseon:
        ganseon[a].append(b)
    else:
        ganseon[a] = [b]
    if b in ganseon:
        ganseon[b].append(a)
    else:
        ganseon[b] = [a]


def tracking(num):
    global count
    if num not in ganseon:
        return
    for i in ganseon[num]:
        if not visited[int(i)]:
            visited[int(i)] = True
            count += 1
            tracking(i)


tracking("1")
print(count)
