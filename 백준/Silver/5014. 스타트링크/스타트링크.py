from collections import deque

f,s,g,u,d = map(int, input().split())
vis = [0] * (f + 1)
vis[s] = 1
dx = [u, -d]

def bfs():
    global f, s, g, u, d
    q = deque()
    q.append(s)
    while q:
        s = q.popleft()
        if s == g:
            print(vis[s] - 1)
            return
        for i in range(len(dx)):
            x = s + dx[i]
            if x < 1 or x > f:
                continue
            if vis[x]:
                continue
            vis[x] = vis[s] + 1
            q.append(x)
    if vis[g] == 0:
        print('use the stairs')

def Solution():
    global f, s, g, u, d
    if s == g:
        print(0)
        return
    bfs()
Solution()