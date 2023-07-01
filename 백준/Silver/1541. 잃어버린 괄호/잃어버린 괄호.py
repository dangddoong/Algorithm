import sys

readl = sys.stdin.readline
sick = list(readl().split("-"))
answer = sum(list(map(int, sick[0].split("+")))) # -가 나오기 전까지의 결과값


if len(sick) == 1: # 식에 +밖에 없으면
    print(answer)
else:
    for i in range(1, len(sick)):
        answer -= sum(list(map(int, sick[i].split("+"))))
    print(answer)
