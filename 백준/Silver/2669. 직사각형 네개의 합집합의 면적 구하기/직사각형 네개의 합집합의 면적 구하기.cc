#include <iostream>
using namespace std;

int x, y, xx, yy, a[101][101];
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    for (int i = 0; i < 4; i++) {
        cin >> x >> y >> xx >> yy;
        for (int i = y; i < yy; i++) {
            for (int j = x; j < xx; j++) {
                a[i][j] = 1;
            }
        }
    }
    int res = 0;
    for (int i = 0; i < 101; i++) {
        for (int j = 0; j < 101; j++) {
            if (a[i][j] == 1) res++;
        }
    }
    cout << res;
}