import sys
from collections import deque

readl = sys.stdin.readline
S = deque(list(readl().rstrip()))
answer, stack = [], []
while S:
    if S[0] == "<":
        answer.append(S.popleft())
        while S[0] != ">":
            answer.append(S.popleft())
        answer.append(S.popleft())
    else:
        while True:
            if len(S) == 0 or S[0] == " " or S[0] == "<":
                break
            stack.append(S.popleft())
        while stack:
            answer.append(stack.pop())
        if S and S[0] == " ":
            answer.append(S.popleft())
print(''.join(answer))
