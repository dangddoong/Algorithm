import sys
readl = sys.stdin.readline
n = int(readl())
word_list = [[] for _ in range(50)]
answer = ""

for _ in range(n):
    word = readl().rstrip()
    word_list[len(word)-1].append(word)

for i in range(50):
    if len(word_list[i]) != 0:
        for k in sorted(set(word_list[i])):
            answer += (k + "\n")

print(answer)
