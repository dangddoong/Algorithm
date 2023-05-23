import sys
readl = sys.stdin.readline
answer = ""

while True:
    stack = []
    string = readl().rstrip()
    if string == ".":
        break
    
    for j in string:
        if j == "(" or j == "[":
            stack.append(j)
        elif j == ")":
            if len(stack) == 0:
                stack.append("wrong")
                break
            elif stack.pop() != "(":
                stack.append("wrong")
                break
        elif j == "]":
            if len(stack) == 0:
                stack.append("wrong")
                break
            elif stack.pop() != "[":
                stack.append("wrong")
                break
    if len(stack) == 0:
        answer += "yes\n"
    else:
        answer += "no\n"
        
print(answer)