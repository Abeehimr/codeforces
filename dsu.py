class dsu:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n

    def find(self, x):
        p = x
        while self.par[p] != p:
            p = self.par[p]
        while self.par[x] != x:
            self.par[x], x = p, self.par[x]
        return p

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
        else:
            self.par[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
        return True