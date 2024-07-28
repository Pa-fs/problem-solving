#include<bits/stdc++.h>
using namespace std;

int dist[100001];
queue<int> q;
int n, k;
int dx[3] = {-1, 1, 2};
int res;
int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    cin >> n >> k;

    if(n == k) {
        cout << 0;
        return 0;
    }
    q.push(n);

    while(dist[k] == 0) {
        int cur = q.front(); q.pop();
        for(int i = 0; i < 3; i++) {
            int x = 0;
            if(i != 2) x = cur + dx[i];
            else x = cur * dx[i];

            if(x < 0 || x > 100000) continue;
            if(dist[x] > 0) continue;
            dist[x] = dist[cur] + 1;
            q.push(x);
        } 
    }
    cout << dist[k];
}
