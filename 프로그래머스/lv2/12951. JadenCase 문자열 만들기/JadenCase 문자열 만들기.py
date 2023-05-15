def solution(s):
    string = s.lower()
    answer = ' '
    for str in string:
        if str.isalpha() and answer[-1] == ' ':
            answer += str.upper()
        else:
            answer += str
    return answer[1:]