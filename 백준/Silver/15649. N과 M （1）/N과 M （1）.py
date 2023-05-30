import sys
readl = sys.stdin.readline
n, m = map(int,readl().split())
isincluded = [False for _ in range(n+1)]
answer = []


def tracking(depth, nums):
    if depth == m:
        answer.append(' '.join(nums))
    else:
        for i in range(n):
            nums_copy = nums.copy()
            if isincluded[i] == False:
                isincluded[i] = True
                nums_copy.append(str(i+1))
                tracking(depth + 1, nums_copy)
                isincluded[i] = False


tracking(0, [])
print('\n'.join(answer))
