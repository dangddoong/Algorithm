import sys
from collections import deque

readl = sys.stdin.readline
t = int(readl())

for _ in range(t):
    case = list(readl().rstrip())
    deq = deque()
    is_break = False
    for _ in range(len(case)):
        a = case.pop()
        if a == "(":
            if len(deq) == 0 or deq.popleft() != ")":
                print("NO")
                is_break = True
                break
        else:
            deq.appendleft(a)
    if is_break:
        continue
    if len(deq) == 0:
        print("YES")
    else:
        print("NO")

