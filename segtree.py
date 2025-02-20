
class SegmentTree:
    def __init__(self, n: int,defult = 0,func = max, idx_comp = None , str_protocol = False) -> None:
        self.tree = [defult]*(2*n)
        self.n = n
        self.str_protocol = str_protocol
        self.func = func
        self.defult = defult
        if idx_comp is not None:
            self._idx_hash(idx_comp)


    def _idx_hash(self,arr):
        self.idx = {}
        for i in range(self.n):
            v = arr[i]
            if self.str_protocol:
                v = str(v)
            self.idx[v] = i

    def make(self,l):
        for i,v in enumerate(l):
            self.tree[self.n + i] = v

        for i in range(self.n-1,0,-1):
            self.tree[i] = self.func(self.tree[2*i],self.tree[2*i+1])

    def _get_index(self,i: int) -> int:
        if hasattr(self,'idx'):
            if self.str_protocol:
                i = str(i)
            if i not in self.idx:
                raise IndexError
            i = self.idx[i]

        if i >= self.n or i < -1:
            raise IndexError
        return i

    def sum(self,l = None , r = None) -> int:
        l = (self._get_index(l) + self.n) if l is not None else (self.n)
        r = (self._get_index(r) + self.n) if r is not None else (2*self.n - 1)

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
        i = self._get_index(i) + self.n
        self.tree[i] = v
        i >>= 1
        while i >= 1:
            self.tree[i] = self.func(self.tree[2*i],self.tree[2*i+1])
            i >>= 1


        


if __name__ == '__main__':
    s = SegmentTree(5)
    s.add(0,[4,1])
    s.add(1,[5,3])
    s.add(2,[4,1])
    print(s.sum(0,4))
