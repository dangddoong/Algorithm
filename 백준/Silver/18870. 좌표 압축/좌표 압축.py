import sys

readl = sys.stdin.readline
n = int(readl())
x_list = list(map(int, readl().split()))
dictionary = {}
x_sort = sorted(list(set(x_list)))
less_case = 0
for num in x_sort:
    dictionary[num] = less_case
    less_case += 1

answer = []
for num in x_list:
    answer.append(dictionary[num])
print(*answer)
