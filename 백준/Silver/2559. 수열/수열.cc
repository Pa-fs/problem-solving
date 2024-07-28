#include<iostream>
#include<algorithm>
using namespace std;

int a[100001], res = -10000001, tmp, n, k;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
	cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		cin >> tmp;
		a[i] = a[i - 1] + tmp;
	}

	for (int i = k; i <= n; i++) {
		res = max(res, a[i] - a[i - k]);
	}
	cout << res << "\n";
    return 0;
}