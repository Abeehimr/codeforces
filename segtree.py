
class SegmentTree:
    def __init__(self, n: int,defult = 0,func = max) -> None:
        self.tree = [defult]*(2*n)
        self.n = n
        self.func = func
        self.defult = defult


    def make(self,l):
        for i,v in enumerate(l):
            self.tree[self.n + i] = v

        for i in range(self.n-1,0,-1):
            self.tree[i] = self.func(self.tree[2*i],self.tree[2*i+1])


    def sum(self,l = None , r = None) -> int:
        l = (l + self.n) if l is not None else (self.n)
        r = (r + self.n) if r is not None else (2*self.n - 1)

        sm = self.defult
        while l <= r:
            if l&1 == 1:
                sm = self.func(sm,self.tree[l])
                l += 1
                
            if r&1 == 0:
                sm = self.func(sm,self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return sm



    def add(self,i: int , v) -> None:
        i = i + self.n
        self.tree[i] = v
        i >>= 1
        while i >= 1:
            self.tree[i] = self.func(self.tree[2*i],self.tree[2*i+1])
            i >>= 1


class LazySegTree:
    def __init__(self, n, ID, LID):
        self.n = n
        self.ID = ID      # identity for merge
        self.LID = LID    # identity for lazy
        self.st = [ID] * (4 * n)
        self.lz = [LID] * (4 * n)

    # ===== CUSTOMIZE THESE 3 =====
    def merge(self, a, b):
        return a + b

    def apply(self, p, v, l, r):
        # range add affects sum by (len * v)
        self.st[p] += (r - l + 1) * v

    def compose(self, oldV, newV):
        # range add: add lazies
        return oldV + newV
    # =============================

    def push(self, p, l, r):
        if self.lz[p] == self.LID:
            return
        m = (l + r) // 2
        lc, rc = p * 2, p * 2 + 1

        self.apply(lc, self.lz[p], l, m)
        self.apply(rc, self.lz[p], m + 1, r)

        self.lz[lc] = self.compose(self.lz[lc], self.lz[p])
        self.lz[rc] = self.compose(self.lz[rc], self.lz[p])

        self.lz[p] = self.LID

    def build(self, a, p=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.st[p] = a[l]
            return
        m = (l + r) // 2
        self.build(a, p * 2, l, m)
        self.build(a, p * 2 + 1, m + 1, r)
        self.st[p] = self.merge(self.st[p * 2], self.st[p * 2 + 1])

    def upd(self, ql, qr, v, p=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.apply(p, v, l, r)
            self.lz[p] = self.compose(self.lz[p], v)
            return

        self.push(p, l, r)
        m = (l + r) // 2
        self.upd(ql, qr, v, p * 2, l, m)
        self.upd(ql, qr, v, p * 2 + 1, m + 1, r)
        self.st[p] = self.merge(self.st[p * 2], self.st[p * 2 + 1])

    def qry(self, ql, qr, p=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:
            return self.ID
        if ql <= l and r <= qr:
            return self.st[p]

        self.push(p, l, r)
        m = (l + r) // 2
        left = self.qry(ql, qr, p * 2, l, m)
        right = self.qry(ql, qr, p * 2 + 1, m + 1, r)
        return self.merge(left, right)


# ===== Example usage (same as your C++) =====
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    st = LazySegTree(n, ID=0, LID=0)
    st.build(a)

    st.upd(2, 5, 3)      # add +3 on [2..5]
    print(st.qry(0, 4))  # sum query



if __name__ == '__main__':
    s = SegmentTree(5)
    s.add(0,[4,1])
    s.add(1,[5,3])
    s.add(2,[4,1])
    print(s.sum(0,4))
