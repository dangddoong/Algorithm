import sys
readl = sys.stdin.readline
x,y,w,h = map(int, readl().split())

def small_one(a,b):
    if a > b:
        return b
    else:
        return a

x = small_one(x, w-x)
y = small_one(y, h-y)
print(small_one(x,y))