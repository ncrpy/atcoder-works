#include <bits/stdc++.h>

using namespace std;

int main() {
    long long T, C;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> C;
        if (C % 2) {
            cout << "Odd" << endl;
        } else if (C % 4) {
            cout << "Same" << endl;
        } else {
            cout << "Even" << endl;
        }
    }
    return 0;
}
