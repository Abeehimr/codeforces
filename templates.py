# t cases
for _ in range(int(input().strip())):
    #ignore this ...
    ...
#array of ints
n, = map( int , input().strip().split() )
a = list( map( int , input().strip().split() ) )


#space separated input
_ = map( int , input().strip().split() )

#string input
s = input().strip()

#int input
n = int(input().strip())

#matrix of ints
n,m = map( int , input().strip().split() )
mat = [list(map(int,input().strip().split())) for _ in range(n)]

#matrix of char no space
n,m = map( int , input().strip().split() )
mat = [input().strip() for _ in range(n)]

#matrix of char with space
n,m = map( int , input().strip().split() )
mat = [list(input().strip().split()) for _ in range(n)]

import sys
def ask(a,b):
    print(f'? {a} {b}')
    sys.stdout.flush()
    o = int(input().strip())
    if o == -1: quit()
    return o

par = [i for i in range(n)]
rank = [0]*n

def find(x):
    p = x
    while par[p] != p:
        p = par[p]
    while par[x] != x:
        par[x] , x = p , par[x]
    return p

def union(x,y):
    px,py = find(x),find(y)
    if px == py:
        return False
    if rank[px] > rank[py]:
        par[py] = px
    else:
        par[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1
    return True


class Fenwick_Tree:
    def __init__(self, n: int, idx_comp = None | list[int], str_protocol = False) -> None:
        self.tree = [0]*n
        self.n = n
        self.str_protocol = str_protocol
        if idx_comp is not None:
            self._idx_hash(idx_comp)


    def _idx_hash(self,arr):
        self.idx = {}
        for i in range(self.n):
            v = arr[i]
            if self.str_protocol:
                v = str(v)
            self.idx[v] = i


    def sum(self,i: int) -> int:
        if hasattr(self,'idx'):
            if self.str_protocol:
                i = str(i)
            if i not in self.idx:
                raise IndexError
            i = self.idx[i]

        if i >= self.n or i < -1:
            raise IndexError
        out = 0
        while i >= 0:
            out += self.tree[i]
            i = (i&(i+1))-1
        return out

    def add(self,i: int , v: int) -> None:
        if hasattr(self,'idx'):
            if self.str_protocol:
                i = str(i)
            if i not in self.idx:
                raise IndexError
            i = self.idx[i]

        if i >= self.n or i < -1:
            raise IndexError
        
        while i < self.n:
            self.tree[i] += v
            i |= i + 1



from heapq import heappush, heappop
class Hold:
    def __init__(self,n,s) -> None:
        self.h = []
        self.n = n
        self.sm = s

    def add(self,v):
        if len(self.h) < self.n:
            heappush(self.h,v)
            self.sm += v        
        else:
            heappush(self.h,v)
            self.sm += v - heappop(self.h)
    
    def q(self):
        return self.sm
    

def nextPermutation(nums):
    i = len(nums) - 2
    while(nums[i] >= nums[i+1] and i > -1):
        i -= 1
    if i == -1:
        nums.reverse()
        return    
    j = len(nums) - 1
    while (nums[i] >= nums[j] and i < j):
        j-= 1
    nums[i],nums[j] = nums[j],nums[i]
    nums[i+1:] = nums[i+1:][::-1]


class PolynomialHash:
    def __init__(self, s: str, A = 911382323, B = 972663749):
        self.s = s
        self.A = A
        self.B = B
        self.n = len(s)
        self.h = [0] * self.n
        self.p = [0] * self.n
        self._precompute()
    
    def _precompute(self):
        """Precompute hash values and power values."""
        self.h[0] = ord(self.s[0]) % self.B
        self.p[0] = 1
        for i in range(1, self.n):
            self.p[i] = (self.p[i - 1] * self.A) % self.B
            self.h[i] = (self.h[i - 1] * self.A + ord(self.s[i])) % self.B
    
    def get_hash(self, a: int, b: int) -> int:
        """Get the hash of substring s[a...b]."""
        if a == 0:
                return self.h[b]
        return (self.h[b] - self.h[a - 1] * self.p[b - a + 1]) % self.B
    

class latin:
    def __init__(self):
        self.h = [0]*26
    
    def add(self,c):
        self.h[ord(c)-ord('a')] += 1

    def remove(self,c):
        self.h[ord(c)-ord('a')] -= 1

    def __eq__(self,other):
        return self.h == other.h

    def contains(self,other):
        for i in range(26):
            if self.h[i] < other.h[i]:
                return False
        return True
    
    def copy(self,other):
        self.h = other.h.copy()

    def cnt(self):
        return sum(self.h)
    
    def __repr__(self):
        return str(self.h)