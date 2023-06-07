import sys
readl = sys.stdin.readline

n, k = map(int, readl().split())
coins = [0]
for _ in range(n):
    coins.append(int(readl()))

now_sum, count = 0, 0

while True:
    if now_sum == k:
        print(count)
        exit()
    if now_sum + coins[n] > k:
        n -= 1
        continue
    now_sum = now_sum + coins[n]
    count += 1