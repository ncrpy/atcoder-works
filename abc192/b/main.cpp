#include <bits/stdc++.h>

using namespace std;

int main() {
    string S;
    string ans = "Yes";
    cin >> S;
    for (int i = 0; i < (int)S.size(); i++) {
        if ((i & 1) ^ (bool)isupper(S.at(i))) {
            ans = "No";
            break;
        }
    }
    cout << ans << endl;

    return 0;
}
