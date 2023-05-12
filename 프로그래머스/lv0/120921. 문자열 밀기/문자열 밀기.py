def solution(A, B):
    # A 길이만큼 for문 돌리고 
    # if(A == B) 
    for i in range(len(A)):
        if(A == B):
            return i
        A = A[-1] + A[0:-1]
    return -1