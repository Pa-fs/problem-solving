#include<bits/stdc++.h>
using namespace std;

int T, n, m, k;
queue<pair<int, int>> q;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};
int b[51][51];
int dist[51][51];
void bfs(int x, int y) {
    q.push({x, y});

    while(!q.empty()) {
        auto cur = q.front(); q.pop();
        for(int dir = 0; dir < 4; dir++) {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];
            if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if(dist[nx][ny] >= 0 || b[nx][ny] == 0) continue;
            dist[nx][ny] = dist[cur.first][cur.second] + 1;
            q.push({nx,ny});
        }
    }
}
int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    cin >> T;
    while(T--) {
        cin >> m >> n >> k;
        int res = 0;
        for(int i = 0; i < n; i++) {
            fill(b[i], b[i] + m, 0);
            fill(dist[i], dist[i] + m, -1);
        }
        for(int i = 0; i < k; i++) {
            int c, d;
            cin >> c >> d;
            b[d][c] = 1;
        }
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(dist[i][j] == -1 && b[i][j] == 1) {
                    bfs(i, j);
                    dist[i][j] = 0;
                    res++;
                }
            }
        }
        cout << res << "\n";
    }

}
