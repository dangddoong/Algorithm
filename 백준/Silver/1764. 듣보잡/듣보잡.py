import sys
readl = sys.stdin.readline

n, m = map(int, readl().split())
dict = {}
answer = []
count = 0

for _ in range(n):
    people = readl().rstrip()
    dict[people] = 0

for _ in range(m):
    people = readl().rstrip()
    first = people[0]
    if people in dict:
        answer.append(people)

answer.sort()
print(len(answer))
print('\n'.join(answer))
