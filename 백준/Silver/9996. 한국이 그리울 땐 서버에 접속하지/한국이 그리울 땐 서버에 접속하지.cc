#include <bits/stdc++.h>
using namespace std;
int n;
string str, s;

int main(){
	cin >> n >> s;
	int pos = s.find('*'); 
	string prx = s.substr(0, pos);
	string sfx = s.substr(pos + 1);
	for(int i = 0; i < n; i++) {
		cin >> str;
		if(str.size() < prx.size() + sfx.size()) {
			cout << "NE\n";
			continue;	
		}
		string strPrx = str.substr(0, prx.size());
		string strSfx = str.substr(str.size() - sfx.size());
		
		if(strPrx == prx && strSfx == sfx) cout << "DA\n";
		else cout << "NE\n";
	}
	return 0;
}
