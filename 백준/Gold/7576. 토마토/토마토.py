import sys
from collections import deque

readl = sys.stdin.readline
m, n = map(int, readl().split())
box = [list(map(int, readl().split())) for _ in range(n)]
not_ripe, period = 0, 0  # 익지않은 토마토 개수, 익는 기간
deq = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            not_ripe += 1
        elif box[i][j] == 1:
            deq.append((j, i))  # j ->가로, i ->세로

if not_ripe == 0:  # 모든 토마토가 익어있는 상태
    print(0)
    exit()

while deq:
    for _ in range(len(deq)):
        x, y = deq.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= m or yy < 0 or yy >= n:
                continue
            if box[yy][xx] == 0:
                box[yy][xx] = 1
                deq.append((xx, yy))
                not_ripe -= 1
    period += 1

if not_ripe == 0:
    print(period-1)  # 마지막에 한바퀴를 더 돌기에 -1해준다. (while문에 break를 둬도 되지만 매번 체크하는게 싫어서..)
else:
    print(-1)
