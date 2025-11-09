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


#2d prefix sum
def prefixSum2D(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(1,n):
        mat[i][0] += mat[i-1][0]
    for j in range(1,m):
        mat[0][j] += mat[0][j-1]
    for i in range(1,n):
        for j in range(1,m):
            mat[i][j] += mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
    return mat

#range sum query
def rangeSum(mat, r1, c1, r2, c2):
    sm = mat[r2][c2]
    if r1 > 0:
        sm -= mat[r1-1][c2]
    if c1 > 0:
        sm -= mat[r2][c1-1]
    if r1 > 0 and c1 > 0:
        sm += mat[r1-1][c1-1]
    return sm

class Fenwick_Tree:
    def __init__(self, n: int) -> None:
        self.tree = [0]*n
        self.n = n



    def sum(self,i: int) -> int:
        out = 0
        while i >= 0:
            out += self.tree[i]
            i = (i&(i+1))-1
        return out

    def add(self,i: int , v: int) -> None:        
        while i < self.n:
            self.tree[i] += v
            i |= i + 1



    

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
    
