def solution(polynomial):
    answer = ""
    valX = 0
    val = 0
    polynomial = polynomial.split('+')
    for elem in polynomial:
        elem = elem.strip()
        if "x" in elem:
            if len(elem) != 1:
                valX = valX + int(elem[:-1])
            else:
                valX = valX + 1
        else:
            val = val + int(elem)
    if valX != 0:
        if valX == 1:
            if val != 0:
                answer += "x + " + str(val)
            else:
                answer += "x"
        else:
            if val != 0:
                answer += str(valX) + "x + " + str(val)
            else:
                answer += str(valX) + "x"
            
            
    else:    
        if val != 0:
            answer += str(val)
    return answer