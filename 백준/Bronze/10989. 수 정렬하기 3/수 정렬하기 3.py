import sys
readl = sys.stdin.readline
n = int(readl())
l = [0] * 10001

for _ in range(n):
    l[int(readl())] += 1
    
for i in range(10001):
    if l[i] != 0:
        for _ in range(l[i]):
            sys.stdout.write(str(i)+'\n')