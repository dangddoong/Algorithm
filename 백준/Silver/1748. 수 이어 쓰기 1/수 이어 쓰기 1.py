import sys
n = sys.stdin.readline().rstrip()
count = 0
len = len(n)
if len == 1:
    print(int(n))
else:
    for i in range(len):
        count += (1 + i) * 9 * (10 ** i)
    count -= len * (9 * (10 ** (len - 1)) - int(n) + int('9' * (len - 1)))
    print(count)