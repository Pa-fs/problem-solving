#include<bits/stdc++.h>
using namespace std;

int r, c;
string b[1001];
int dist1[1001][1001]; // fire
int dist2[1001][1001]; // person
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
queue<pair<int, int>> q1;
queue<pair<int, int>> q2;
void bfs1() {
    while(!q1.empty()) {
        auto cur = q1.front(); q1.pop();
        for(int dir = 0; dir < 4; dir++) {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];

            if(nx < 0 || ny < 0 || nx >= r || ny >= c) continue;
            if(dist1[nx][ny] >= 0 || b[nx][ny] == '#') continue;
            dist1[nx][ny] = dist1[cur.first][cur.second] + 1;
            q1.push({nx,ny});
        }
    }
}

int bfs2() {
    while(!q2.empty()) {
        auto cur = q2.front(); q2.pop();
        for(int dir = 0; dir < 4; dir++) {
            int nx = cur.first + dx[dir];
            int ny = cur.second + dy[dir];

            if(nx < 0 || ny < 0 || nx >= r || ny >= c) {
                return dist2[cur.first][cur.second] + 1;
            }
            if(dist2[nx][ny] >= 0 || b[nx][ny] == '#') continue;
            if(dist1[nx][ny] != -1 && dist1[nx][ny] <= dist2[cur.first][cur.second] + 1) continue;
            dist2[nx][ny] = dist2[cur.first][cur.second] + 1;
            q2.push({nx,ny});
        }
    }

    return 0;
}
int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    cin >> r >> c;
    for(int i = 0; i < r; i++) cin >> b[i];
    for(int i = 0; i < r; i++) {
        fill(dist1[i], dist1[i] + c, -1);
        fill(dist2[i], dist2[i] + c, -1);
    }
    // fire
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            if(b[i][j] == 'F') {
                dist1[i][j] = 0;
                q1.push({i,j});
            }
        }
    }
    // person
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            if(b[i][j] == 'J') {
                dist2[i][j] = 0;
                q2.push({i,j});
            }
        }
    }
    int res = 0;
    bfs1();
    res = bfs2();
    if(res) {
        cout << res;
    } else {
        cout << "IMPOSSIBLE";
    }
}
