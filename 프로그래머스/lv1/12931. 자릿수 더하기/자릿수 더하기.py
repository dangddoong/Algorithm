def solution(n):
    string_n = str(n)
    answer = 0
    for i in range(len(string_n)):
        answer += int(string_n[i])
    return answer