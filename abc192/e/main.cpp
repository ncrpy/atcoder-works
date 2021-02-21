#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, M, X, Y;
    cin >> N >> M >> X >> Y;
    X--;
    Y--;

    vector<vector<array<int, 3>>> G(N);
    for (int i = 0; i < M; i++) {
        int A, B, T, K;
        cin >> A >> B >> T >> K;
        A--;
        B--;
        G.at(A).push_back({B, T, K});
        G.at(B).push_back({A, T, K});
    }

    // Dijkstra
    vector<long long> dist(N, 1e18);
    dist.at(X) = 0;
    priority_queue<pair<long long, int>, vector<pair<long long, int>>,
                   greater<pair<long long, int>>>
        Q;
    Q.push({0, X});
    while (!Q.empty()) {
        auto [dv, v] = Q.top();
        Q.pop();
        if (dv > dist.at(v)) {
            continue;
        }
        for (auto [u, t, k] : G.at(v)) {
            long long du = (dv + k - 1) / k * k + t;
            if (du < dist.at(u)) {
                dist.at(u) = du;
                Q.push({du, u});
            }
        }
    }

    cout << (dist.at(Y) < 1e18 ? dist.at(Y) : -1) << endl;

    return 0;
}
