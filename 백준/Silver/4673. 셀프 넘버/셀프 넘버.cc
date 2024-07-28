#include<iostream>
using namespace std;
bool a[10036];
void d() {
	for (int i = 1; i <= 10000; i++) {
		int res = i;
		int n = i;
		int sum = 0;
		while (n > 0) {
			int d = n % 10;
			sum += d;
			n /= 10;
		}
		res += sum;
		a[res] = true;
	}
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
	d();
	for (int i = 1; i <= 10000; i++) if (a[i] == 0) cout << i << "\n";
	return 0;
}