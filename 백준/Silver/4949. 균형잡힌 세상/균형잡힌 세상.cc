#include<bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    while(true) {
        string s;
        getline(cin, s);
        if(s == ".") break;
        stack<char> S;
        bool isTrue = true;
        for(auto ch : s) {
            if(ch == '(' || ch == '[') {
                S.push(ch);
            }
            else if(ch == ')') {
                if(S.empty() || S.top() != '(') {
                    isTrue = false;
                    break;
                } else S.pop();
            }
            else if(ch == ']') {
                if(S.empty() || S.top() != '[') {
                    isTrue = false;
                    break;
                } else S.pop();
            }
        }

        if(S.empty() && isTrue) cout << "yes" << "\n";
        else cout << "no" << "\n";
    }
}