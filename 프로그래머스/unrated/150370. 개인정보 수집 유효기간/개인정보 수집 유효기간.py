# 풀이 1
def solution(today, terms, privacies):
    answer = []
    dic = {}
    today = list(map(int, today.split('.')))
    todayCount = today[2] + today[1] * 28 + today[0] * 28 * 12 # 일자 기준으로 합산해서 비교하기 위함

    for term in terms:
        termsType, expirationDate = term.split()
        dic[termsType] = int(expirationDate) * 28 # 유효 개월수도 일자로 변환해서 타입별로 저장

    for i in range(len(privacies)):
        collectionDate, termsType = privacies[i].split()
        collectionDate = list(map(int, collectionDate.split('.')))
        collectionDateCount = collectionDate[2] + collectionDate[1] * 28 + collectionDate[0] * 28 * 12
        if todayCount >= collectionDateCount + dic[termsType]: # 오늘 날짜가 가입일+유효기간 보다 크거나 같다면 == 만료됐다면 
            answer.append(i+1)

    return answer



# 풀이 2
def solution(today, terms, privacies):
    dic = {}
    answer = []
    for term in terms:
        termsType, expirationDate = term.split()
        dic[termsType] = expirationDate
    for i in range(len(privacies)):
        collectionDate, termsType = privacies[i].split()
        if isPersonalInfoExpired(today, dic[termsType], collectionDate):
            answer.append(i + 1)
    return answer


def isPersonalInfoExpired(strToday, strExpirationMonth, strCollectionDate):
    todayYear, todayMonth, todayDay = map(int, strToday.split('.'))
    expirationYear, expirationMonth, expirationDay = map(int, strCollectionDate.split('.'))
    expirationMonth += int(strExpirationMonth) % 12
    expirationYear += int(strExpirationMonth) // 12
    if expirationMonth > 12:
        expirationYear += 1
        expirationMonth -= 12
        
    if todayYear > expirationYear:
        return True
    if todayYear == expirationYear and todayMonth > expirationMonth:
        return True
    if todayYear == expirationYear and todayMonth == expirationMonth and todayDay >= expirationDay:
        return True
    return False

