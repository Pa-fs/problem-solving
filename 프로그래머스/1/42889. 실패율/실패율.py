def solution(N, stages):
    # 도전자
    ch = [0] * (N + 2)
    for stage in stages:
        ch[stage] += 1
    
    # 길이
    total = len(stages)
    fails = {}
    
    for stage in range(1, N + 1):
        if ch[stage] == 0:
            fails[stage] = 0
        else:
            fails[stage] = ch[stage] / total
        total -= ch[stage]
    
    fails = sorted(fails, key=lambda x: fails[x], reverse=True)
    return fails