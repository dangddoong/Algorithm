import sys
readl = sys.stdin.readline
n, m = map(int, readl().split())


def tracking(depth, answer):
    if depth == m:
        for num_list in answer:
            if depth == 1:
                print(num_list[0])
            else:
                print(' '.join(num_list))
        return
    elif depth == 0:
        for i in range(1, n+1):
            answer.append([str(i)])
        tracking(depth+1, answer)
    else:
        new_answer = []
        for j in answer:
            for k in range(1, n+1):
                copy = j.copy()
                copy.append(str(k))
                new_answer.append(copy)
        tracking(depth+1, new_answer)


tracking(0,[])
