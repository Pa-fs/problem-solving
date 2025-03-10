def solution(participant, completion):
    answer = ''
    dic = {}
    
    for person in participant:
        if person in dic:
            dic[person] += 1
        else:
            dic[person] = 1
    for person in completion:
        if person in dic:
            dic[person] += 1
        else:
            dic[person] = 1
    for key, val in dic.items():
        if val % 2 != 0:
            answer = key
            break
    return answer