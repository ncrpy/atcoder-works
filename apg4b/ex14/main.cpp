#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> v(3);
    for (int i = 0; i < 3; i++) {
        cin >> v.at(i);
    }
    int max = *max_element(v.begin(), v.end());
    int min = *min_element(v.begin(), v.end());
    cout << max - min << endl;
    return 0;
}
