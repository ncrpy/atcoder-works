#include <bits/stdc++.h>

using namespace std;

int main() {
    int A, B;
    string op;

    cin >> A >> op >> B;
    if (op == "+") {
        cout << A + B;
    } else if (op == "-") {
        cout << A - B;
    } else if (op == "*") {
        cout << A * B;
    } else if (op == "/" && B) {
        cout << A / B;
    } else {
        cout << "error";
    }
    cout << endl;

    return 0;
}
