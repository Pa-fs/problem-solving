#include<bits/stdc++.h>
using namespace std;

int s[2][7];
int n, k, res;
int main() {
    cin >> n >> k;
    for(int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        s[a][b]++;
    }

    for(int i = 0; i < 2; i++) {
        for(int j = 1; j < 7; j++) {
            res = res + s[i][j] / k;
            if(s[i][j] % k) res++;
        }
    }
    cout << res;
}