def solution(n):
    answer = [n * [0] for _ in range(n)]
    # print(answer)
    
    val = 1
    y, x = 0, 0
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    dir = 0
    while val <= n * n:
        answer[y][x] = val
        val += 1
        ny = y + dy[dir]
        nx = x + dx[dir]
        if ny < 0 or ny >= n or nx < 0 or nx >= n or answer[ny][nx] != 0:
            dir = (dir + 1) % 4
            ny = y + dy[dir]
            nx = x + dx[dir]
        y = ny
        x = nx
        
    return answer