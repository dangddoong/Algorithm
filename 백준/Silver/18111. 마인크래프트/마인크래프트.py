import sys

readl = sys.stdin.readline
n, m, b = map(int, readl().split())
dic = {}
minimum, maximum = 256, 0
answer = {'time': -1, 'height': 0}

for _ in range(n):
    line = list(map(int, readl().split()))
    minimum = min(minimum, min(line))
    maximum = max(maximum, max(line))
    for num in line:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1


for height in range(minimum, maximum+1):
    total_time = 0
    block = b
    for key in dic.keys():
        if height > key:
            total_time += dic[key] * 1 * (height - key)
            block -= dic[key] * (height - key)
        elif height < key:
            total_time += dic[key] * 2 * (key - height)
            block += dic[key] * (key - height)
    if (answer['time'] == -1 or answer['time'] >= total_time) and block >= 0:
        answer['time'] = total_time
        answer['height'] = height
        
print(answer['time'], answer['height'])
