import sys

readl = sys.stdin.readline
num_exist = [False] * 21
m = int(readl())

for _ in range(m):
    orders = readl().split()
    if len(orders) == 1:
        orders = orders[0]
    else:
        orders, num = orders[0], int(orders[1])

    if orders == "add":
        num_exist[num] = True
    elif orders == "remove":
        num_exist[num] = False
    elif orders == "check":
        if num_exist[num]:
            print(1)
        else:
            print(0)
    elif orders == "toggle":
        num_exist[num] = not num_exist[num]
    elif orders == "all":
        for i in range(20):
            num_exist[i+1] = True
    else:
        for i in range(20):
            num_exist[i + 1] = False

