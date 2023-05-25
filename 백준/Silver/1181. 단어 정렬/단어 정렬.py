import sys
readl = sys.stdin.readline
n = int(readl())
word_list = [[[] for _ in range(26)] for _ in range(50)]
answer = ""

for _ in range(n):
    word = readl().rstrip()
    first_ord = ord(word[0]) - ord('a')
    if word not in word_list[len(word)-1][first_ord]:
        word_list[len(word)-1][first_ord].append(word)

for i in range(50):
    for j in range(26):
        if len(word_list[i][j]) != 0:
            for k in sorted(word_list[i][j]):
                answer += (k + "\n")

print(answer)
