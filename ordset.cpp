#include <bits/stdc++.h>
using namespace std;

#include <bits/extc++.h>
using namespace __gnu_pbds;
template<class T>
using Tree = tree<T, null_type, less<T>, rb_tree_tag,
tree_order_statistics_node_update>;

int main() {
    Tree<int> os;
    auto res = os.insert(5); // returns pair<iterator,bool>
    cout << res.second << "\n";   // true if inserted
    cout << *res.first << "\n";   // iterator to element (5)
    os.insert(1);
    os.insert(10);
    // kth element (0-indexed)
    auto it = os.begin();
    cout << *(it = os.find_by_order(1)) << "\n"; // 5
    os.erase(it);
    // number of elements < x
    cout << os.order_of_key(6) << "\n";   // 2 (1,5)
    // lower_bound / upper_bound
    cout << *os.lower_bound(6) << "\n";   // 10
    cout << *os.upper_bound(5) << "\n";   // 10
}
