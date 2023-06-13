import sys


def d(num):
    double = num * 2
    if double > 9999:
        double = double % 10000
    return double


def s(num):
    minus_one = num - 1
    if num == 0:
        minus_one = 9999
    return minus_one


def l(num):
    str_num = str(num)
    # 4자리수가 아닐 때를 위한 line
    str_num = "0" * (4 - len(str_num)) + str_num
    left = int(str_num[1:] + str_num[:-3])
    return left


def r(num):
    str_num = str(num)
    # 4자리수가 아닐 때를 위한 line
    str_num = "0" * (4 - len(str_num)) + str_num
    right = int(str_num[3:] + str_num[:-1])
    return right


readl = sys.stdin.readline
t = int(readl())

for _ in range(t):
    a, b = map(int, readl().split())
    visted = [False] * 10000
    db = {a: []}
    find = False
    while not find:
        db_copy = db.copy()
        db = {}
        for num in db_copy:
            result = d(num)
            if not visted[result]:
                db[result] = db_copy[num].copy()
                db[result].append("D")
                visted[result] = True
            if result == b:
                print(''.join(db[result]))
                find = True
                break
                
            result = s(num)
            if not visted[result]:
                db[result] = db_copy[num].copy()
                db[result].append("S")
                visted[result] = True
            if result == b:
                print(''.join(db[result]))
                find = True
                break
            
            result = l(num)
            if not visted[result]:
                db[result] = db_copy[num].copy()
                db[result].append("L")
                visted[result] = True
            if result == b:
                print(''.join(db[result]))
                find = True
                break

            result = r(num)
            if not visted[result]:
                db[result] = db_copy[num].copy()
                db[result].append("R")
                visted[result] = True
            if result == b:
                print(''.join(db[result]))
                find = True
                break

