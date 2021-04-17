#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<string> S(3);
    for (int i = 0; i < 3; i++) {
        cin >> S.at(i);
    }
    vector<char> lst;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < (int)S.at(i).size(); j++) {
            lst.push_back(S.at(i).at(j));
        }
    }
    sort(lst.begin(), lst.end());
    lst.erase(unique(lst.begin(), lst.end()), lst.end());
    int n = (int)lst.size();
    if (n > 10) {
        cout << "UNSOLVABLE" << endl;
        return 0;
    }


    return 0;
}
