import sys
readl = sys.stdin.readline
N = int(readl())
abilities = [list(map(int, readl().split())) for _ in range(N)]
min_difference = sys.maxsize
visited = [False for _ in range(N)]

def makeTeamB(teamA):
    teamB = []
    for i in range(N):
        if not visited[i]:
            teamB.append(i)
    return teamB

def tracking(depth, index, teamA):
    global min_difference
    if depth == N // 2:
        teamB = makeTeamB(teamA)
        sumA, sumB = 0, 0
        for i in teamA:
            for j in teamA:
                sumA += abilities[i][j]
        for a in teamB:
            for b in teamB:
                sumB += abilities[a][b]
        min_difference = min(min_difference, abs(sumA - sumB))
        return
    for i in range(index, N):
        if not visited[i]:
            visited[i] = True
            t = teamA.copy()
            t.append(i)
            tracking(depth+1, i+1, t)
            visited[i] = False


tracking(0,0,[])
print(min_difference)
