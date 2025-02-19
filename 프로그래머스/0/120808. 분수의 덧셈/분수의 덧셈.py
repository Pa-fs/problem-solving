def solution(numer1, denom1, numer2, denom2):
    answer = []
    # 일단 곱하고 최대공약수로 나눈다
    numer3 = (numer1 * denom2) + (numer2 * denom1)
    denom3 = (denom1 * denom2)
    if numer3 == denom3:
        return [1, 1]
    div = 1
    for val in range(1, denom3 + 1):
        if numer3 % val == 0 and denom3 % val == 0:
            div = val
    return [numer3 // div, denom3 // div]