#include <bits/stdc++.h>

using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    int d = B - A;
    int ans;
    for (int i = 1; i <= d; i++) {
        int a = (A - 1) / i;
        int b = B / i;
        if (b - a > 1) {
            ans = i;
        }
    }
    cout << ans << endl;

    return 0;
}
