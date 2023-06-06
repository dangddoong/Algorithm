import sys
readl = sys.stdin.readline


def dfs(depth, idx):
    if depth == 6:
        print(*answer)
        return

    for i in range(idx, k):
        answer.append(S[i])
        dfs(depth + 1, i + 1)
        answer.pop()


while True:
    array = list(map(int, readl().split()))
    k = array[0]
    S = array[1:]
    answer = []
    if k == 0:
        exit(0)

    dfs(0, 0)
    print()
