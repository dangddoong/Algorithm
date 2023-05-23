import sys
from collections import deque
readl = sys.stdin.readline
s1 = list(readl().rstrip())
m = int(readl())
s2 = deque()

for _ in range(m):
    command = readl()
    if command[0] == "P":
        s1.append(command[2])
    elif command[0] == "L":
        if len(s1) != 0:
            s2.appendleft(s1.pop())
    elif command[0] == "D":
        if len(s2) != 0:
            s1.append(s2.popleft())
    elif command[0] == "B":
        if len(s1) != 0:
            s1.pop()

print(''.join(s1+list(s2)))