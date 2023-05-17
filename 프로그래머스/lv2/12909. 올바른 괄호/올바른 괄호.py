def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False
    return True

    # answer = 0
    #for a in s:
    #    if a == "(":
    #        answer += 1
    #    else:
    #        if answer < 1: 
    #            return False
    #        answer -= 1
    #
    # if answer == 0:
    #    return True
    #return False