def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def solution(numer1, denom1, numer2, denom2):
    denom_lcm = denom1*denom2 // gcd(denom1, denom2)
    answer_numer = numer1*(denom_lcm//denom1) + numer2*(denom_lcm//denom2)
    numer_demon_gcd =  gcd(denom_lcm, answer_numer)
    return [answer_numer//numer_demon_gcd, denom_lcm//numer_demon_gcd]