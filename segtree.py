
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



class LazySegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.s = [0] * (4 * self.n)   # sum
        self.z = [0] * (4 * self.n)   # lazy
        self._build(1, 0, self.n - 1, arr)

    def _build(self, k, x, y, arr):
        if x == y:
            self.s[k] = arr[x]
            return
        d = (x + y) // 2
        self._build(2 * k, x, d, arr)
        self._build(2 * k + 1, d + 1, y, arr)
        self.s[k] = self.s[2 * k] + self.s[2 * k + 1]

    def _push(self, k, x, y):
        if self.z[k] != 0:
            d = (x + y) // 2
            v = self.z[k]

            # propagate to left child
            self.s[2 * k] += (d - x + 1) * v
            self.z[2 * k] += v

            # propagate to right child
            self.s[2 * k + 1] += (y - d) * v
            self.z[2 * k + 1] += v

            self.z[k] = 0

    def add(self, a, b, u):
        self._add(a, b, u, 1, 0, self.n - 1)

    def _add(self, a, b, u, k, x, y):
        if b < x or a > y:
            return

        if a <= x and y <= b:
            self.s[k] += (y - x + 1) * u # idhar tak propagate ho jaega
            self.z[k] += u # propagate down nai hua
            return

        self._push(k, x, y)

        d = (x + y) // 2
        self._add(a, b, u, 2 * k, x, d)
        self._add(a, b, u, 2 * k + 1, d + 1, y)
        self.s[k] = self.s[2 * k] + self.s[2 * k + 1]

    def sum(self, a, b):
        return self._sum(a, b, 1, 0, self.n - 1)

    def _sum(self, a, b, k, x, y):
        if b < x or a > y:
            return 0

        if a <= x and y <= b:
            return self.s[k]

        self._push(k, x, y)

        d = (x + y) // 2
        return (
            self._sum(a, b, 2 * k, x, d)
            + self._sum(a, b, 2 * k + 1, d + 1, y)
        )




if __name__ == '__main__':
    s = SegmentTree(5)
    s.add(0,[4,1])
    s.add(1,[5,3])
    s.add(2,[4,1])
    print(s.sum(0,4))
