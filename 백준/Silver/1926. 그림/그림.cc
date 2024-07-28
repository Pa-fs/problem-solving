#include<bits/stdc++.h>
using namespace std;
int b[501][501];
int vis[501][501];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
queue<pair<int, int>> q;
int n, m;
int bfs(int x, int y) {
    int size = 0;
    q.push({x, y});
    vis[x][y] = 1;

    while(!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();

        for(int dir = 0; dir < 4; dir++) {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];
            if(nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
            if(vis[nx][ny] || b[nx][ny] == 0) continue;
            vis[nx][ny] = 1;
            q.push({nx,ny});
        }
        size++;
    }

    return size;
}
int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    cin >> n >> m;

    int res = 0, cnt = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> b[i][j];
        }
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(vis[i][j] == 0 && b[i][j] == 1) {
                res = max(res, bfs(i, j));
                cnt++;
            }
        }
    }

    cout << cnt << "\n";
    cout << res << "\n";
}