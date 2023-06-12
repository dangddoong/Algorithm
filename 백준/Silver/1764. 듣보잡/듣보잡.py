import sys
readl = sys.stdin.readline

n, m = map(int, readl().split())
dict = {}
answer = {}
count = 0

for _ in range(n):
    people = readl().rstrip()
    dict[people] = 0

for _ in range(m):
    people = readl().rstrip()
    first = people[0]
    if people in dict:
        count += 1
        if first in answer:
            answer[first].append(people)
        else:
            answer[first] = [people]

# Python3.6부터는 딕셔너리가 입력순대로 정렬됨
print(count)
for key in sorted(answer):
    answer[key].sort()
    print('\n'.join(answer[key]))
