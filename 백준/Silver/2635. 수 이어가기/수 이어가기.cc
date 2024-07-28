#include<iostream>
using namespace std;
int n, tmpDth;
void go(int fst, int snd, int dth, bool f) {
    if (f) cout << fst << " ";
    int cur = fst - snd;
    if (cur < 0) {
        if(f) cout << snd << " ";
        tmpDth = dth;
        return;
    }
    go(snd, cur, dth + 1, f);
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    int secNum = n;
    int maxDth = 1;
    for (int i = 0; i <= n; i++) {
        tmpDth = 0;
        go(n, i, 1, false);
        if (maxDth < tmpDth) {
            maxDth = tmpDth;
            secNum = i;
        }
    }
    cout << maxDth + 1 << "\n";
    go(n, secNum, 1, true);
    
    return 0;
}