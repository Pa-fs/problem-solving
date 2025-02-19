def solution(answers):
    lst = []
    
    person = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5,]]
    cnt = [0] * 3
    
    for i, answer in enumerate(answers):
        for j in range(len(person)):
            if answer == person[j][i % len(person[j])]:
                cnt[j] += 1
    
    maxx = -1
    for i, val in enumerate(cnt):
        if maxx < val:
            maxx = val

    for i, val in enumerate(cnt):
        if maxx == val:
            lst.append(i + 1)
    return lst