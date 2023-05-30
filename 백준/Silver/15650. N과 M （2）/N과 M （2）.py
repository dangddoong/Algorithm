import sys
readl = sys.stdin.readline
n, m = map(int, readl().split())
answer = []

def tracking(depth, index, nums):
    if depth == m:
        answer.append(' '.join(nums))
    else:
        for i in range(index, n):
            nums_copy = nums.copy()
            nums_copy.append(str(i+1))
            tracking(depth+1, i+1, nums_copy)

tracking(0,0,[])
print('\n'.join(answer))
