import sys
from collections import deque
readl = sys.stdin.readline
n = int(readl())
deque = deque()
answer = 0
while n!=0:
    deque.append(n%2)
    n = n//2
while len(deque)!=0:
    answer = answer*2
    answer += deque.popleft()
print(answer)