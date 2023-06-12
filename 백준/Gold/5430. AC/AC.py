from collections import deque
import sys
readl = sys.stdin.readline

t = int(readl())

for _ in range(t):
    p = readl().rstrip()
    n = int(readl())
    str_x = readl().rstrip()
    deq = deque()
    num = ""
    do_reverse, is_err = False, False

    if n != 0:
        deq = deque(str_x[1:-1].split(','))

    for order in p:
        if order == "R":
            do_reverse = not do_reverse
        else:
            if not deq:
                print("error")
                is_err = True
                break
            if do_reverse:
                deq.pop()
            else:
                deq.popleft()
    if not is_err:
        answer = list(deq)
        if do_reverse:
            answer.reverse()
            print("[" + ','.join(answer) + "]")
        else:
            print("[" + ','.join(answer) + "]")
