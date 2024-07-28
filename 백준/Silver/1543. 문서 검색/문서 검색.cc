#include<iostream>
#include<string>
using namespace std;

string s, tmp;
int split(string o, string del) {
    string t = "";
    int pos = 0;
    int res = 0;
    while ((pos = o.find(del)) != string::npos) {
        t = o.substr(0, pos);
        o.erase(0, pos + del.length());
        res++;
    }
    return res;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    getline(cin, s);
    getline(cin, tmp);
    cout << split(s, tmp);
    return 0;
}