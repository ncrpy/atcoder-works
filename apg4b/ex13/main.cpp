#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, sum;
    cin >> N;

    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A.at(i);
    }

    sum = accumulate(A.begin(), A.end(), 0);
    for (int i = 0; i < N; i++) {
        cout << abs(A.at(i) - sum / N) << endl;
    }

    return 0;
}
