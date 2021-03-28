#include <bits/stdc++.h>

#define MOD 998244353

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long long> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A.at(i);
    }
    sort(A.begin(), A.end());
    long long ans = 0;
    long long s = 0;
    for (int i = 0; i < N; i++) {
        s += A.at(i) * (1 << i);
    }
    for (int i = 0; i < N; i++) {
        s -= A.at(i);
        s /= 2;
        ans += A.at(i) * (A.at(i) + s);
        ans %= MOD;
    }
    cout << ans << endl;
    return 0;
}
