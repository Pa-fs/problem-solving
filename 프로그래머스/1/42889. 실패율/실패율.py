def solution(N, stages):
    c = [0] * (N + 2) 
    for stage in stages:
        c[stage] += 1
    
    fails = {}
    total = len(stages)
    
    for stage in range(1, N + 1):
        if c[stage] == 0:
            fails[stage] = 0
        else:
            fails[stage] = c[stage] / total
            total = total - c[stage]
    
    res = sorted(fails, key=lambda x: fails[x], reverse=True)
    return res