#include<iostream>
using namespace std;

int n, m, k, app, lo, hi, res;
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m >> k;
    lo = 1;
    for (int i = 0; i < k; i++) {
        cin >> app;
        hi = lo + m - 1;
        if (app >= lo && app <= hi) continue;
        else {
            if (app < lo) {
                res += lo - app;
                lo = app;
            }
            else {
                res += app - hi;
                lo += app - hi;
            }
        }
    }
    cout << res << "\n";
    return 0;
}