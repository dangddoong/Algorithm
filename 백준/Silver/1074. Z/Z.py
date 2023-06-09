# 탑다운 방식으로 풀어보기,
# 4등분했을 때 좌상단부터 우하단 순서로 x는 0~3이고
# 각 블럭이 [ x * (한 변의 길이의 제곱) / 4 ]의 값을 가진다는 점에 착안해 풀어보았음.

import sys
readl = sys.stdin.readline
n, r, c = map(int, readl().split())
answer = 0


while n != 0:
    # 4등분했을 때 어느 블럭에 속하는지에 따라 그에 맞는 값을 더해줌
    length = 2 ** n
    if r > (length - 1) / 2:
        if c > (length - 1) / 2:
            answer += 3 * (length ** 2) // 4
            c -= 2 ** (n-1)
        else:
            answer += 2 * (length ** 2) // 4
        r -= 2 ** (n-1)
    else:
        if c > (length - 1) / 2:
            answer += 1 * (length ** 2) // 4
            c -= 2 ** (n-1)
        else:
            answer += 0
    n -= 1


print(answer)