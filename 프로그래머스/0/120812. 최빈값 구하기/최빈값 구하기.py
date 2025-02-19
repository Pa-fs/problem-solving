def solution(array):
    answer = 0
    count = [0] * 1000
    for elem in array:
        count[elem] += 1
    maxx = -1
    maxi = -1
    for i, val in enumerate(count):
        if maxx < val:
            maxx = val
            maxi = i
            count[i] = 0
    for i, val in enumerate(count):
        if maxx == val:
            return -1

    return maxi