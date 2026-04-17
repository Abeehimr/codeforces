class Line:
    def __init__(self, m=0, c=float('inf')):
        self.m, self.c = m, c
    def eval(self, x):
        return self.m * x + self.c

class LiChaoTree:
    def __init__(self, min_x, max_x, get_min=True):
        self.min_x, self.max_x = min_x, max_x
        self.tree = {}
        self.get_min = get_min

    def add_line(self, new):
        l, r, node = self.min_x, self.max_x, 1
        while l <= r:
            if node not in self.tree:
                self.tree[node] = new
                return
            cur = self.tree[node]
            mid = (l + r) // 2
            left_new, left_cur = new.eval(l), cur.eval(l)
            mid_new, mid_cur = new.eval(mid), cur.eval(mid)
            left_better = left_new < left_cur if self.get_min else left_new > left_cur
            mid_better = mid_new < mid_cur if self.get_min else mid_new > mid_cur
            
            if mid_better:
                self.tree[node], new = new, cur

            if left_better != mid_better:
                node = node * 2
                r = mid
            else:
                node = node * 2 + 1
                l = mid + 1

    def query(self, x):
        l, r, node = self.min_x, self.max_x, 1
        best = float('inf')
        while l <= r and node in self.tree:
            if self.get_min:
                best = min(best, self.tree[node].eval(x))
            else:
                best = max(best, self.tree[node].eval(x))
                
            mid = (l + r) // 2
            if x <= mid:
                node = node * 2
                r = mid
            else:
                node = node * 2 + 1
                l = mid + 1
        return best

# Example usage
lct = LiChaoTree(-100000, 100000)
lct.add_line(Line(3, 5))
lct.add_line(Line(-2, 4))
lct.add_line(Line(1, 1))

print("Min at x=2:", lct.query(2))
print("Min at x=-1:", lct.query(-1))
