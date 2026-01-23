#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 998244353;
const ll G = 3;

ll modpow(ll a, ll e) {
    ll r = 1;
    while (e) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}

void ntt(vector<ll> & a, bool invert) {
    int n = a.size();
    static vector<int> rev;
    static vector<ll> roots{0,1};

    if ((int)rev.size() != n) {
        int k = __builtin_ctz(n);
        rev.assign(n, 0);
        for (int i = 0; i < n; i++)
            rev[i] = (rev[i>>1] >> 1) | ((i&1) << (k-1));
    }
    if ((int)roots.size() < n) {
        int k = __builtin_ctz(roots.size());
        roots.resize(n);
        while ((1 << k) < n) {
            ll e = modpow(G, (MOD-1) >> (k+1));
            for (int i = 1 << (k-1); i < (1 << k); i++) {
                roots[2*i] = roots[i];
                roots[2*i+1] = roots[i] * e % MOD;
            }
            k++;
        }
    }

    for (int i = 0; i < n; i++)
        if (i < rev[i])
            swap(a[i], a[rev[i]]);

    for (int len = 1; len < n; len <<= 1) {
        for (int i = 0; i < n; i += 2*len) {
            for (int j = 0; j < len; j++) {
                ll u = a[i+j];
                ll v = a[i+j+len] * roots[len+j] % MOD;
                a[i+j] = (u + v) % MOD;
                a[i+j+len] = (u - v + MOD) % MOD;
            }
        }
    }

    if (invert) {
        reverse(a.begin()+1, a.end());
        ll inv_n = modpow(n, MOD-2);
        for (ll & x : a)
            x = x * inv_n % MOD;
    }
}

vector<ll> multiply_ntt(vector<ll> &a, vector<ll> &b) {
    vector<ll> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    int n = 1;
    while (n < (int)a.size() + (int)b.size()) n <<= 1;
    fa.resize(n);
    fb.resize(n);

    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; i++)
        fa[i] = fa[i] * fb[i] % MOD;
    ntt(fa, true);
    return fa;
}
