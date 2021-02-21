#include <bits/stdc++.h>

using namespace std;

int f(int x);

int f(int x) {
    string s2 = to_string(x);
    sort(s2.begin(), s2.end());
    string s1 = s2;
    reverse(s1.begin(), s1.end());
    return stoi(s1) - stoi(s2);
}

int main() {
    int N, K;
    cin >> N >> K;
    for (int i = 0; i < K; i++) {
        N = f(N);
        if (N == 0) {
            break;
        }
    }
    cout << N << endl;

    return 0;
}
