def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    gcd = max(numer, denom)
    
    for i in range(gcd, 0, -1):
        if (numer % i == 0) and (denom % i == 0):
            gcd = i
            break
    
    answer.append(numer / gcd)
    answer.append(denom / gcd)
    return answer