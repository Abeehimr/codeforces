#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void solve() {
    int N; cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    sort(A.begin(), A.end());
    vector<int> vs;
    if (A.front()) vs.push_back(A.front());
    int i = 0;
    while (i < N) {
        int j = i;
        while (j < N and A.at(i) == A.at(j)) ++j;
        vs.push_back(j - i);
        i = j;
        if (i < N) {
            vs.push_back(A.at(i) - A.at(i - 1));
        }
    }
    reverse(vs.begin(), vs.end());
    bool lose = true;
    for (int v : vs) {
        if (lose) {
            lose ^= 1;
        } else {
            if (v == 1) lose ^= 1;
        }
    }
    cout << (lose ? "Bob" : "Alice") << '\n';
}
int main() {
    int T; cin >> T;
    while(T--) solve();
}
