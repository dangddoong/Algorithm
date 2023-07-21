import sys

readl = sys.stdin.readline
n = int(readl())
dictionary = {}

for _ in range(n):
    age, name = readl().split()
    age = int(age)
    
    if age in dictionary:
        dictionary[age].append(name)
    else:
        dictionary[age] = [name]

keys = sorted(list(dictionary.keys()))

for key in keys:
    for name in dictionary[key]:
        print(key, name)
