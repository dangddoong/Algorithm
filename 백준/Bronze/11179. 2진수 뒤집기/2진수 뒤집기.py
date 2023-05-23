# 맛있게 풀기
import sys
readl = sys.stdin.readline
n = int(readl())
answer = 0

while n!=0:
    answer = answer*2 + (n%2)
    n = n//2
    
print(answer)



#  deque로 풀기
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
