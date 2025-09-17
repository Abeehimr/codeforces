
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


        


if __name__ == '__main__':
    s = SegmentTree(5)
    s.add(0,[4,1])
    s.add(1,[5,3])
    s.add(2,[4,1])
    print(s.sum(0,4))
