import sys 

readl = sys.stdin.readline
N, M = map(int, readl().split())
tree = list(map(int, readl().split()))
start, end = 1, max(tree)  

while start <= end:  
    mid = (start + end) // 2

    log = 0  
    for i in tree:
        if i >= mid:
            log += i - mid

    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)