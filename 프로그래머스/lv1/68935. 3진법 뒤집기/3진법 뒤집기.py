def solution(n):
    jinsu = []
    answer = 0
    while n!=0:
        jinsu.append(n%3)
        n=n//3
    for i in range(len(jinsu)):
        answer += (3**(len(jinsu)-i-1)) * jinsu[i]
    return answer