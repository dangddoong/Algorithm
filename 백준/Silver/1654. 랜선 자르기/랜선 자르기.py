import sys

readl = sys.stdin.readline
k, n = map(int, readl().split())
li = []
total_len = 0

for _ in range(k):
    num = int(readl())
    li.append(num)
    total_len += num
start = 1
end = total_len // n  #그리디하게 풀기
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for num in li:
        cnt += (num // mid)
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
