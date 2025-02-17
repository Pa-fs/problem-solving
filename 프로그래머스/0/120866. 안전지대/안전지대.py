def search(board, x, y):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    for dir in range(0, 8):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board):
            continue
        if board[nx][ny] == 2 and board[nx][ny] == 1:
            continue
        if board[nx][ny] == 0:
            board[nx][ny] = 2
        

def solution(board):
    answer = 0
    # 반복하며 지뢰(1) 찾기
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                search(board, i, j)
                    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                answer += 1
    return answer