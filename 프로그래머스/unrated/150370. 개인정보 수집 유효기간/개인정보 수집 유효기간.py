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