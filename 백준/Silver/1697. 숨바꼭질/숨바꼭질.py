from collections import deque
n, k = map(int, input().split())
dx = [-1, 1, 2]
vis = [0] * 200001
def bfs():
    global n, k
    q = deque()
    q.append(n)
    vis[n] = 1
    while q:
        cur = q.popleft()
        if cur == k:
            break
        for i in range(len(dx)):
            if dx[i] == 2:
                nx = cur * dx[i]
            else:
                nx = cur + dx[i]
            if nx < 0 or nx > 100001:
                continue
            if vis[nx]:
                continue
            vis[nx] = vis[cur] + 1
            q.append(nx)
    print(vis[k] - 1)
def Solution():
    bfs()
Solution()