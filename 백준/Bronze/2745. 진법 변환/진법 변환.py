import sys
readl = sys.stdin.readline
N,B = readl().split()
answer = 0
lenN = len(N)
intB = int(B)
for i in range(lenN):
    if N[i].isalpha():
        answer += (ord(N[i])-ord("A")+10)*(intB**(lenN-i-1))
    else:
        answer += int(N[i])*(intB**(lenN-i-1))
print(answer)