import sys

readl = sys.stdin.readline

r_list = [1]
for i in range(1, int(readl())):
    r_list.append(r_list[i-1] * 31)
s = readl().rstrip()
ord_a = ord('a')
answer = 0

for i in range(len(s)):
    answer += (ord(s[i]) - ord_a + 1) * r_list[i]

print(answer % 1234567891)


# import sys

# readl = sys.stdin.readline

# r_list = [1]
# for i in range(1, int(readl())):
#     r_list.append(r_list[i-1] * 31)
# s = readl().rstrip()
# answer = 0

# for i in range(len(s)):
#     answer += (ord(s[i]) - ord('a') + 1) * r_list[i]

# print(answer)
