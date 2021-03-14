#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> A(M), B(M);
    for (int i = 0; i < M; i++) {
        cin >> A.at(i) >> B.at(i);
    }

    vector<vector<char>> ret(N, vector<char>(N, '-'));
    for (int i = 0; i < M; i++) {
        int a = A.at(i) - 1;
        int b = B.at(i) - 1;
        ret.at(a).at(b) = 'o';
        ret.at(b).at(a) = 'x';
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << ret.at(i).at(j);
            cout << ((j == N - 1) ? '\n' : ' ');
        }
    }

    return 0;
}
