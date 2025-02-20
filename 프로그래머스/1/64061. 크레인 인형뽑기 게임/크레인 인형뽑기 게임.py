def solution(board, moves):
    answer = 0
    stack = []
    
    board2 = [[0] * len(board) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            board2[i][j] = board[j][i]
                
    for move in moves:
        for i in range(len(board2[move - 1])):
            if board2[move - 1][i] == 0:
                continue
            if stack and stack[-1] == board2[move - 1][i]:
                stack.pop()
                answer += 2;
            else:
                stack.append(board2[move - 1][i])
            board2[move - 1][i] = 0
            break
    return answer