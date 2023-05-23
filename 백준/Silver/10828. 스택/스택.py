import sys
readl = sys.stdin.readline
n = int(readl())
stack = []
answer = ""

for _ in range(n):
    command = readl().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack)==0:
            answer += "-1\n"
        else:
            answer += stack.pop() + "\n"
    elif command[0] == "size":
        answer += str(len(stack)) + "\n"
    elif command[0] == "empty":
        if len(stack)==0:
            answer += "1\n"
        else:
            answer += "0\n"
    elif command[0] == "top":
        if len(stack)==0:
            answer += "-1\n"
        else:
            answer += stack[-1] + "\n"
print(answer)