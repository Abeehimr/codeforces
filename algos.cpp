#include <bits/stdc++.h>
using namespace std;

#define int long long
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define len(x) (int)(x).size()
#define ph push_back
#define pp pop_back
#define ln cout << endl

template<typename T>
using heap = priority_queue<T, vector<T>, greater<T>>;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<bool> vb;
const int MOD = 1e9 + 7;

void tarjan(int N, vector<vi>& adj, vector<vi>& out) {
    stack<int> st;
    vb onst(N, false);
    vi id(N,-1);
    vi low(N,-1);
    int cur = 0;

    function <void(int)> dfs = [&] (int u) -> void {
        st.push(u);
        onst[u] = true;
        id[u] = low[u] = cur++;

        for (int v: adj[u]) {
            if (id[v] == -1) dfs(v);
            if (onst[v]) low[u] = min(low[u], low[v]);
        }
        if (id[u] == low[u]) {
            vi comp;
            while (1) {
                int x = st.top(); st.pop();
                comp.ph(x);
                onst[x] = false;
                if (x == u) break;
            }
            out.ph(comp);
        }
    };

    rep(i,0, N) {
        if (id[i] == -1) dfs(i);
    }
}

void bridges(int N, vector<vi>& adj, vector<pii>& out) {
    vi id(N, -1), low(N, -1);
    int cur = 0;
    function<void(int,int)> dfs = [&](int u, int parent) {
        id[u] = low[u] = cur++;
        for (int v : adj[u]) {
            if (v == parent) continue;

            if (id[v] == -1) {
                dfs(v, u);
                low[u] = min(low[u], low[v]);
                if (low[v] > id[u]) {
                    out.push_back({u, v});
                }
            } else {
                low[u] = min(low[u], id[v]);
            }
        }
    };
    rep(i,0,N) if (id[i] == -1) dfs(i, -1);
}

void articulation_points(int N, vector<vi>& adj, vb& is_cut) {
    vi id(N, -1), low(N, -1);
    int cur = 0;
    function<void(int,int)> dfs = [&](int u, int parent) {
        id[u] = low[u] = cur++;
        int children = 0;
        for (int v : adj[u]) {
            if (v == parent) continue;
            if (id[v] == -1) {
                children++;
                dfs(v, u);
                low[u] = min(low[u], low[v]);
                if (parent != -1 && low[v] >= id[u]) {
                    is_cut[u] = true;
                }
            } else low[u] = min(low[u], id[v]);
        }
        if (parent == -1 && children > 1) is_cut[u] = true;
    };
    rep(i,0,N) if (id[i] == -1) dfs(i, -1);
}

signed main() {

}