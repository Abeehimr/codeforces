
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


class PersistantNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class PersistantSegTree:
    def __init__(self, n):
        self.n = n
        self.T = [PersistantNode()]

    def build(self, arr, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.T[node].val = arr[l]
            return
        m = (l + r) // 2
        self.T[node].left = len(self.T)
        self.T.append(PersistantNode())
        self.build(arr, self.T[node].left, l, m)

        self.T[node].right = len(self.T)
        self.T.append(PersistantNode())
        self.build(arr, self.T[node].right, m + 1, r)

        self.T[node].val = self.T[self.T[node].left].val + self.T[self.T[node].right].val
    
    def update(self, idx, val, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            new_node = PersistantNode(val)
            self.T.append(new_node)
            return len(self.T) - 1
        m = (l + r) // 2
        new_node = PersistantNode()
        self.T.append(new_node)
        new_idx = len(self.T) - 1

        if idx <= m:
            self.T[new_idx].left = self.update(idx, val, self.T[node].left, l, m)
            self.T[new_idx].right = self.T[node].right
        else:
            self.T[new_idx].left = self.T[node].left
            self.T[new_idx].right = self.update(idx, val, self.T[node].right, m + 1, r)

        self.T[new_idx].val = self.T[self.T[new_idx].left].val + self.T[self.T[new_idx].right].val
        return new_idx
    
    def query(self, ql, qr, node=0, l=0, r=None):
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.T[node].val
        m = (l + r) // 2
        left_sum = self.query(ql, qr, self.T[node].left, l, m)
        right_sum = self.query(ql, qr, self.T[node].right, m + 1, r)
        return left_sum + right_sum




if __name__ == '__main__':
    s = SegmentTree(5)
    s.add(0,[4,1])
    s.add(1,[5,3])
    s.add(2,[4,1])
    print(s.sum(0,4))
