import sys
sys.setrecursionlimit(10 ** 9)

maps = []
m, n = map(int, input().split())  # n과 m을 입력받음 (예: 5 6)
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# n개의 줄에 대해 데이터를 입력받아 2차원 리스트에 추가
for _ in range(m):
    row = list(map(int, input().strip()))  # 한 줄을 입력받고 공백을 제거 후 정수로 변환
    maps.append(row)
vis = [[0] * n for _ in range(m)]
res = False

def dfs(y, x):
    global res
    if res:
        return

    if y == m - 1:
        for i in range(n):
            if x == i:
                res = True
                return

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if ny < 0 or ny >= m or nx < 0 or nx >= n or vis[ny][nx] or maps[ny][nx] == 1:
            continue
        vis[ny][nx] = 1
        dfs(ny, nx)


def Solution():
    for i in range(n):
        if maps[0][i] == 0:
            dfs(0, i)
    if res:
        print("YES")
    else:
        print("NO")
Solution()