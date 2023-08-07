import sys

readl = sys.stdin.readline
m, n = map(int, readl().split())

if m == 1 or m == 2:
    print(2)
if m % 2 == 0:
    m = m+1
    
for i in range(m, n+1, 2):
    if i == 1:
        continue

    is_decimal = True
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            is_decimal = False
            break
    if is_decimal:
        print(i)


