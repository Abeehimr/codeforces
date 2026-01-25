#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct Dinic {
    struct Edge {
        int to;
        ll cap;
        int rev;
        ll flow;
    };

    int n;
    vector<vector<Edge>> g;
    vector<int> level, it;

    Dinic(int n) : n(n), g(n), level(n), it(n) {}

    // add directed edge u -> v with capacity cap
    void addEdge(int u, int v, ll cap) {
        Edge a{v, cap, (int)g[v].size(), 0};
        Edge b{u, 0,   (int)g[u].size(), 0};
        g[u].push_back(a);
        g[v].push_back(b);
    }
    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        queue<int> q;
        level[s] = 0;
        q.push(s);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto &e : g[u]) {
                if (e.cap - e.flow > 0 && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
            }
        }
        return level[t] != -1;
    }
    ll dfs(int u, int t, ll f) {
        if (u == t) return f;
        for (int &i = it[u]; i < (int)g[u].size(); i++) {
            Edge &e = g[u][i];
            if (e.cap - e.flow > 0 && level[e.to] == level[u] + 1) {
                ll pushed = dfs(e.to, t, min(f, e.cap - e.flow));
                if (pushed) {
                    e.flow += pushed;
                    g[e.to][e.rev].flow -= pushed;
                    return pushed;
                }
            }
        }
        return 0;
    }
    ll maxflow(int s, int t) {
        ll flow = 0;
        while (bfs(s, t)) {
            fill(it.begin(), it.end(), 0);
            while (ll pushed = dfs(s, t, LLONG_MAX))
                flow += pushed;
        }
        return flow;
    }
    // get all edges of the min-cut after maxflow
    vector<pair<int,int>> mincut(int s) {
        vector<pair<int,int>> cut;
        vector<bool> visited(n, false);
        queue<int> q;
        q.push(s);
        visited[s] = true;
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto &e : g[u]) {
                if (e.cap - e.flow > 0 && !visited[e.to]) {
                    visited[e.to] = true;
                    q.push(e.to);
                }
            }
        }
        for (int u = 0; u < n; u++) {
            if (!visited[u]) continue;
            for (auto &e : g[u]) {
                if (!visited[e.to] && e.cap > 0) cut.emplace_back(u, e.to);
            }
        }
        return cut;
    }
    // get flows on edges
    vector<tuple<int,int,ll>> edgeFlows() {
        vector<tuple<int,int,ll>> flows;
        for (int u = 0; u < n; u++) {
            for (auto &e : g[u]) {
                if (e.flow > 0) flows.emplace_back(u, e.to, e.flow);
            }
        }
        return flows;
    }
    // reset flows to 0 (reuse graph)
    void resetFlows() {
        for (auto &v : g)
            for (auto &e : v)
                e.flow = 0;
    }
    // clear all edges
    void clear() {
        for (auto &v : g) v.clear();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;           // nodes, edges
    Dinic din(n);

    for (int i = 0; i < m; i++) {
        int u, v; long long c;
        cin >> u >> v >> c;
        u--; v--;              // convert to 0-index
        din.addEdge(u,v,c);
    }

    int s, t;
    cin >> s >> t;           // source, sink
    s--; t--;

    cout << "Max Flow: " << din.maxflow(s,t) << "\n";

    return 0;
}