#include <bits/stdc++.h>
using namespace std;


template <class Node, class Lazy>
struct LazySegTree {
    int n;
    vector<Node> st;
    vector<Lazy> lz;

    Node ID;
    Lazy LID;

    LazySegTree(int n, Node ID, Lazy LID) : n(n), ID(ID), LID(LID) {
        st.assign(4 * n, ID);
        lz.assign(4 * n, LID);
    }

    Node merge(const Node &a, const Node &b) {
        // merge valuee
        return a + b;
    }

    void apply(int p, const Lazy &v, int l, int r) {
        // apply lazy v to st[p] on segment [l..r]
        st[p] += (r - l + 1) * v;
    }

    Lazy compose(const Lazy &oldV, const Lazy &newV) {
        // how to combine lazies:
        return oldV + newV;
    }

    void push(int p, int l, int r) {
        if (lz[p] == LID) return;
        int m = (l + r) >> 1;
        int lc = p << 1, rc = lc | 1;

        apply(lc, lz[p], l, m);
        apply(rc, lz[p], m + 1, r);

        lz[lc] = compose(lz[lc], lz[p]);
        lz[rc] = compose(lz[rc], lz[p]);

        lz[p] = LID;
    }

    void build(const vector<Node> &a, int p, int l, int r) {
        if (l == r) { st[p] = a[l]; return; }
        int m = (l + r) >> 1;

        build(a, p << 1, l, m);
        build(a, p << 1 | 1, m + 1, r);

        st[p] = merge(st[p << 1], st[p << 1 | 1]);
    }

    void build(const vector<Node> &a) { build(a, 1, 0, n - 1); }

    void upd(int ql, int qr, const Lazy &v, int p, int l, int r) {
        if (qr < l || r < ql) return;
        if (ql <= l && r <= qr) {
            apply(p, v, l, r);
            lz[p] = compose(lz[p], v);
            return;
        }
        push(p, l, r);
        int m = (l + r) >> 1;
        upd(ql, qr, v, p << 1, l, m);
        upd(ql, qr, v, p << 1 | 1, m + 1, r);
        st[p] = merge(st[p << 1], st[p << 1 | 1]);
    }

    void upd(int l, int r, const Lazy &v) { upd(l, r, v, 1, 0, n - 1); }

    Node qry(int ql, int qr, int p, int l, int r) {
        if (qr < l || r < ql) return ID;
        if (ql <= l && r <= qr) return st[p];
        push(p, l, r);
        int m = (l + r) >> 1;
        return merge(qry(ql, qr, p << 1, l, m),
                     qry(ql, qr, p << 1 | 1, m + 1, r));
    }

    Node qry(int l, int r) { return qry(l, r, 1, 0, n - 1); }
};

using Node = long long;
using Lazy = long long;
struct Seg : LazySegTree<Node, Lazy> {
    Seg(int n) : LazySegTree(n, 0LL, 0LL) {}

    Node merge(const Node &a, const Node &b) {
        return a + b;
    }
    void apply(int p, const Lazy &v, int l, int r) {
        st[p] += (r - l + 1) * v;
    }
    Lazy compose(const Lazy &oldV, const Lazy &newV) {
        return oldV + newV;
    }
};

int main () {


    int n; cin >> n;
    vector<Node> a(n);
    for (auto &x : a) cin >> x;



    Seg st(n);
    st.build(a);

    st.upd(2, 5, 3);         // add +3 on [2..5]
    cout << st.qry(0, 4);    // sum query

}