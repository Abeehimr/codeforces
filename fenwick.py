class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def ADD(self, i: int, delta: int):
        i += 1  # internally use 1-indexed BIT logic
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def SUM(self, i: int) -> int:
        i += 1  # convert to 1-indexed
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

class RangeBIT:
    def __init__(self, n: int):
        self.n = n
        self.B1 = Fenwick(n)
        self.B2 = Fenwick(n)
        
    # add `val` to range [l, r] (0-indexed)
    def range_add(self, l: int, r: int, val: int):
        self._add(self.B1, l, val)
        self._add(self.B1, r + 1, -val)
        self._add(self.B2, l, val * (l))
        self._add(self.B2, r + 1, -val * (r + 1))

    def _add(self, bit: Fenwick, i: int, delta: int):
        if 0 <= i < self.n: bit.ADD(i, delta)

    def prefix_sum(self, x: int) -> int:
        if x < 0: return 0
        return (x + 1) * self.B1.SUM(x) - self.B2.SUM(x)

    def range_sum(self, l: int, r: int) -> int:
        return self.prefix_sum(r) - self.prefix_sum(l - 1)


class Fenwick_Tree_2D:
    def __init__(self,n,m):
        self.n, self.m = n, m
        self.tree = [[0] * (m + 1) for _ in range(n + 1)]
    def query(self, x, y):
        sum_val = 0
        i = x
        while i >= 0:
            j = y
            while j >= 0:
                sum_val += self.tree[i][j]
                j = (j & (j + 1)) - 1
            i = (i & (i + 1)) - 1
        return sum_val

    def update(self, x, y, delta):
        i = x
        while i < self.n:
            j = y
            while j < self.m:
                self.tree[i][j] += delta
                j |= j + 1
            i |= i + 1

    def range_query(self, x1, y1, x2, y2):
        return (self.query(x2, y2) - self.query(x1 - 1, y2) - self.query(x2, y1 - 1) + self.query(x1 - 1, y1 - 1))