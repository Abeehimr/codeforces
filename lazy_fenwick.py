class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int):
        i += 1  # internally use 1-indexed BIT logic
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i: int) -> int:
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
        if 0 <= i < self.n:
            bit.add(i, delta)

    # prefix sum of a[0..x]
    def prefix_sum(self, x: int) -> int:
        return (x + 1) * self.B1.sum(x) - self.B2.sum(x)

    # range sum of a[l..r]
    def range_sum(self, l: int, r: int) -> int:
        return self.prefix_sum(r) - (self.prefix_sum(l - 1) if l > 0 else 0)
