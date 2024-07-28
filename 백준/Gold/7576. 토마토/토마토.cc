#include<bits/stdc++.h>
using namespace std;

int n, m;
int b[1001][1001];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};
int dist[1001][1001];
queue<pair<int, int>> q;
int res;
int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    cin >> m >> n;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> b[i][j];
            // 시작점이 여러개
            if(b[i][j] == 1) {
                q.push({i, j});
            }
            // 익지 않은 토마토는 dist array -1로 세팅
            // b[i][j] == -1이면 빈 상자임 => dist array = 0으로 방문했다고 생각
            else if(b[i][j] == 0){
                dist[i][j] = -1;
            }
        }
    }

    while(!q.empty()) {
        auto cur = q.front(); q.pop();
        for(int dir = 0; dir < 4; dir++) {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];
            if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if(dist[nx][ny] >= 0) continue;
            dist[nx][ny] = dist[cur.first][cur.second] + 1;
            q.push({nx,ny});
        }
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            // 아직 익지 않은 토마토가 있으면 종료
            if(dist[i][j] == -1) {
                cout << -1;
                return 0;
            }
            // 제일 큰 값이 언제 다 익었는지 나타냄
            res = max(res, dist[i][j]);
        }
    }

    cout << res;
}
