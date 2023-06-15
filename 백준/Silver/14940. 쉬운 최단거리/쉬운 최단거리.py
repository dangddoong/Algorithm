import sys
from collections import deque

readl = sys.stdin.readline
n, m = map(int, readl().split())

maps = []
x, y, distance = 0, 0, 0
already_find = False
deq = deque()

for i in range(n):
    line = list(readl().split())
    maps.append(line)

    if not already_find:
        for j in range(m):
            if line[j] == "2":
                x, y = j, i
                already_find = True

deq.append((x, y, 0))

while deq:
    new_deq = []
    for _ in range(len(deq)):
        x, y, distance = deq.popleft()

        if distance == 1:
            maps[y][x] = '-2'
        else:
            maps[y][x] = str(distance)

        if x < m-1 and maps[y][x + 1] == "1":
            new_deq.append((x + 1, y, distance + 1))
        if x > 0 and maps[y][x - 1] == "1":
            new_deq.append((x - 1, y, distance + 1))
        if y < n-1 and maps[y + 1][x] == "1":
            new_deq.append((x, y + 1, distance + 1))
        if y > 0 and maps[y - 1][x] == "1":
            new_deq.append((x, y - 1, distance + 1))
    deq = deque(set(new_deq))

for line in maps:
    for a in range(m):
        if line[a] == "-2":
            line[a] = "1"
        elif line[a] == "1":
            line[a] = "-1"
    answer = ' '.join(line)
    print(answer)
