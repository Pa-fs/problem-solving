#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int m, n, k, a[101][101], vis[101][101];
int x, y, xx, yy;
int dy[] = { -1, 0, 1, 0 };
int dx[] = { 0, 1, 0, -1 };
vector<int> v;
int dfs(int y, int x) {
    if (vis[y][x] || a[y][x]) return 0;
    vis[y][x] = 1;
    int area = 1;
    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny < 0 || nx < 0 || ny >= n || nx >= m || vis[ny][nx] || a[ny][nx] == 1) continue;
        area += dfs(ny, nx);
    }
    return area;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> m >> n >> k;
    for (int i = 0; i < k; i++) {
        cin >> x >> y >> xx >> yy;
        for (int i = x; i < xx; i++) {
            for (int j = y; j < yy; j++) {
                a[i][j] = 1;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] == 0 && vis[i][j] == 0) {
                v.push_back(dfs(i, j));
            }
        }
    }
    sort(v.begin(), v.end());
    cout << v.size() << "\n";
    for (int d : v) cout << d << " ";
    return 0;
}