import sys
readl = sys.stdin.readline
n = int(readl())
nums = [int(readl()) for _ in range(n)]
base1, base2 = list(range(n, 0, -1)), []
answer = []
index = 0

while index != n:
    if nums[index] in base1:
        base2.append(base1.pop())
        answer.append("+")
    elif base2 and base2[-1] == nums[index]:
            base2.pop()
            answer.append("-")
            index += 1
    else:
        print("NO")
        break
if index == n:
    print("\n".join(answer))
