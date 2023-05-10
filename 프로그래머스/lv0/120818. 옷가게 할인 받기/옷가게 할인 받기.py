import math

def solution(price):
    answer = 0
    if price < 100000:
        answer = price
    elif price < 300000:
        answer = math.trunc(price*0.95)
    elif price < 500000:
        answer = math.trunc(price*0.9)
    else:
        answer = math.trunc(price*0.8)

    return answer