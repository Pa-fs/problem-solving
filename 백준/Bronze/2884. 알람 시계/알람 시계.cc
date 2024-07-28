#include<iostream>
using namespace std;
int h, m;
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
	cin >> h >> m;
	if (h - 1 < 0) {
		if (m - 45< 0) {
			m = (m + 60) - 45;
			h = 23;
		}
		else m = m - 45;
	}
	else {
		if (m - 45 < 0) {
			m = (m + 60) - 45;
			h--;
		}
		else m = m - 45;
	}
	cout << h << " " << m << "\n";
    return 0;
}