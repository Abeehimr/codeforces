from collections import defaultdict

class LCA:
    def __init__(self, n):
        self.n = n
        self.LOG = n.bit_length()  # log2(n) rounded up
        self.up = [[-1] * self.LOG for _ in range(n)]
        self.depth = [0] * n
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def iterative_dfs(self, root):
        stack = [(root, -1)]
        while stack:
            node, parent = stack.pop()
            self.up[node][0] = parent
            for i in range(1, self.LOG):
                if self.up[node][i - 1] != -1:
                    self.up[node][i] = self.up[self.up[node][i - 1]][i - 1]
            
            for neighbor in self.adj[node]:
                if neighbor != parent:
                    self.depth[neighbor] = self.depth[node] + 1
                    stack.append((neighbor, node))

    def preprocess(self, root=0):
        self.iterative_dfs(root)

    def get_lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u  # Ensure u is deeper
        
        # Lift u to the same depth as v
        diff = self.depth[u] - self.depth[v]
        for i in range(self.LOG):
            if diff & (1 << i):
                u = self.up[u][i]
        
        if u == v:
            return u
        
        # Lift both u and v until their parents match
        for i in reversed(range(self.LOG)):
            if self.up[u][i] != self.up[v][i]:
                u = self.up[u][i]
                v = self.up[v][i]
        
        return self.up[u][0]
