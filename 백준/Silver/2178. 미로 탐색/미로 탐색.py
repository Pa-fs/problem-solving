from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
n, m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
q = deque()
res = 0
def bfs():
    q.append([0, 0])
    vis[0][0] = 1
    while q:
        pos = q.popleft()
        y = pos[0]
        x = pos[1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if maps[ny][nx] == 0 or vis[ny][nx] > 0:
                continue
            vis[ny][nx] = vis[y][x] + 1
            q.append([ny, nx])

def Solution():
    bfs()
    print(vis[n - 1][m - 1])
Solution()