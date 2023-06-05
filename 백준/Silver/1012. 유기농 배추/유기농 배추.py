# 계획 -> 구현
# 계획 - 주어진 테스트 케이스에 몇개의 배추 블럭(연결되어 있으면 1블럭)이 있는가를 구한다.
#        -> 상하좌우를 체크하는 함수를 만들고, 입력을 받으면서 근처에 없을시 블럭개수를 추가한다.
# ++ 테스트 케이스가 여러개이므로 입력을 어떻게 받을지도 생각하자
import sys
readl = sys.stdin.readline


def checking(x, y):
    global block_count
    baechu[x][y] = False
    
    if x != 0 and baechu[x-1][y]:
        baechu[x-1][y] = False
        checking(x-1, y)
    if y != 0 and baechu[x][y-1]:
        baechu[x][y-1] = False
        checking(x, y-1)
    if baechu[x+1][y]:
        baechu[x+1][y] = False
        checking(x+1, y)
    if baechu[x][y+1]:
        baechu[x][y+1] = False
        checking(x, y+1)


test_case = int(readl())
for _ in range(test_case):
    m, n, k = map(int, readl().split())
    baechu = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    block_count = 0

    for _ in range(k):
        xx, yy = map(int, readl().split())
        baechu[xx][yy] = True

    for i in range(m):
        for j in range(n):
            if baechu[i][j]:
                block_count += 1
                checking(i, j)
    print(block_count)
