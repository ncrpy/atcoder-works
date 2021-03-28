#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A.at(i);
    }

    vector<int> v;
    int x;
    int y;
    vector<int> w;
    for (int bit = 0; bit < (1 << N); bit++) {
        v.clear();
        x = 0;
        y = 0;
        for (int j = 0; j < N; j++) {
            x |= A.at(j);
            if (bit & (1 << j)) {
                v.push_back(x);
                x = 0;
            }
        }
        v.push_back(x);
        for (int j = 0; j < (int)v.size(); j++) {
            y ^= v.at(j);
        }
        w.push_back(y);
    }

    int ans = *min_element(w.begin(), w.end());
    cout << ans << endl;

    return 0;
}
