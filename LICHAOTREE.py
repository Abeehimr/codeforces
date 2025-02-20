class Line:
    def __init__(self, m=0, c=float('inf')):  # Default to y = ∞
        self.m = m
        self.c = c
    
    def eval(self, x):
        return self.m * x + self.c  # y = mx + c

class LiChaoTree:
    def __init__(self, min_x, max_x):
        self.min_x = min_x
        self.max_x = max_x
        self.tree = {}  # Dictionary to store nodes dynamically

    def add_line(self, new_line):
        """ inserts a new line in the tree """
        l, r = self.min_x, self.max_x
        node = 1
        
        while l <= r:
            if node not in self.tree:
                self.tree[node] = new_line
                return
            
            mid = (l + r) // 2
            cur_line = self.tree[node]

            # Determine where new_line is better
            left_better = new_line.eval(l) < cur_line.eval(l)
            mid_better = new_line.eval(mid) < cur_line.eval(mid)

            if mid_better:
                self.tree[node], new_line = new_line, self.tree[node]

            # Move to the correct half
            if left_better != mid_better:
                node = 2 * node  # Left child
                r = mid
            else:
                node = 2 * node + 1  # Right child
                l = mid + 1

    def query(self, x):
        """finds the minimum y-value at x """
        l, r = self.min_x, self.max_x
        node = 1
        best = float('inf')

        while l <= r and node in self.tree:
            best = min(best, self.tree[node].eval(x))
            mid = (l + r) // 2

            if x <= mid:
                node = 2 * node  # Left child
                r = mid
            else:
                node = 2 * node + 1  # Right child
                l = mid + 1
        return best

# Example Usage
min_x, max_x = -100000, 100000
lct = LiChaoTree(min_x, max_x)

lct.add_line(Line(3, 5))   # y = 3x + 5
lct.add_line(Line(-2, 4))  # y = -2x + 4
lct.add_line(Line(1, 1))   # y = x + 1

print("Min at x=2:", lct.query(2))
print("Min at x=-1:", lct.query(-1))
