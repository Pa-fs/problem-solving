def solution(answers):
    answer = []
    
    # 수포자 찍기리스트
    random_list = [[1,2,3,4,5,], [2,1,2,3,2,4,2,5,], [3,3,1,1,2,2,4,4,5,5]]
    
    # 정답개수 구하기
    person = [0] * 3
    for i in range(len(answers)):
        for j in range(len(random_list)):
            if answers[i] == random_list[j][i % len(random_list[j])]:
                person[j] += 1
    
    # 정답 개수 여럿일 경우 처리
    maxval = max(person)
    for i in range(len(person)):
        if person[i] >= maxval:
            answer.append(i + 1)
    return answer