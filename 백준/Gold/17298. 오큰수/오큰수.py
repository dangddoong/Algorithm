import sys
readl = sys.stdin.readline

n = int(readl())
A = list(map(int, readl().split()))
stack, answer = [], [-1] * n
idx = 0

for i in range(n):
    if stack and A[stack[-1]] < A[i]:
        for _ in range(len(stack)):
            if A[stack[-1]] < A[i]:
                answer[stack.pop()] = A[i]
            else:
                break
        stack.append(i)
    else:
        stack.append(i)
    
print(*answer)
