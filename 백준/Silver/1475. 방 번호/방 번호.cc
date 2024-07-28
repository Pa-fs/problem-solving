#include<bits/stdc++.h>
using namespace std;
int freq[10];
int main() {
    int n, mx = -1e9;
    cin >> n;
    while(n > 0) {
        freq[n % 10]++;
        n = n / 10;
    }
    for(int i = 0; i < 10; i++) {
        if(i == 6 || i == 9) continue;
        mx = max(mx, freq[i]);
    }

    cout << max(mx, (freq[6] + freq[9] + 1) / 2);
}