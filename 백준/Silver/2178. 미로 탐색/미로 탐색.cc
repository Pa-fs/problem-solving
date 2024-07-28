#include<bits/stdc++.h>
using namespace std;

int n, m;
string b[101];
int dist[101][101];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
void bfs() {
    queue<pair<int, int>> q;
    dist[0][0] = 1;
    q.push({0, 0});
 
    while(!q.empty()) {
        auto cur = q.front(); q.pop();
        for(int dir = 0; dir < 4; dir++) {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];

            if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if(dist[nx][ny] >= 0 || b[nx][ny] == '0') continue;
            dist[nx][ny] = dist[cur.first][cur.second] + 1;
            q.push({nx,ny});
        }
    }
}
int main() {
    cin >> n >> m;

    for(int i = 0; i < n; i++) cin >> b[i];
    for(int i = 0; i < n; i++) fill(dist[i], dist[i] + m, -1);
    
    bfs();

    cout << dist[n - 1][m - 1];
}
