from collections import defaultdict

class TarjanSCC:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.timer = 0
        self.stack = []
        self.on_stack = [False] * n
        self.ids = [-1] * n
        self.low = [0] * n
        self.sccs = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, u):
        self.stack.append(u)
        self.on_stack[u] = True
        self.ids[u] = self.low[u] = self.timer
        self.timer += 1

        for v in self.graph[u]:
            if self.ids[v] == -1:  # not visited
                self.dfs(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif self.on_stack[v]:
                self.low[u] = min(self.low[u], self.ids[v])

        # root of SCC
        if self.ids[u] == self.low[u]:
            scc = []
            while True:
                node = self.stack.pop()
                self.on_stack[node] = False
                scc.append(node)
                if node == u: break
            self.sccs.append(scc)

    def find_sccs(self):
        for i in range(self.n):
            if self.ids[i] == -1:
                self.dfs(i)
        return self.sccs



class BridgeFinder:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.timer = 0
        self.tin = [-1] * n
        self.low = [-1] * n
        self.visited = [False] * n
        self.bridges = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, u, p=-1):
        self.visited[u] = True
        self.tin[u] = self.low[u] = self.timer
        self.timer += 1

        for v in self.graph[u]:
            if v == p: continue
            if self.visited[v]:
                self.low[u] = min(self.low[u], self.tin[v])
            else:
                self.dfs(v, u)
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] > self.tin[u]:
                    self.bridges.append((u, v))

    def find_bridges(self):
        for i in range(self.n):
            if not self.visited[i]:
                self.dfs(i)
        return self.bridges


class ArticulationPoints:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.timer = 0
        self.tin = [-1] * n
        self.low = [-1] * n
        self.visited = [False] * n
        self.articulation_points = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, u, p=-1):
        self.visited[u] = True
        self.tin[u] = self.low[u] = self.timer
        self.timer += 1
        children = 0

        for v in self.graph[u]:
            if v == p: continue
            if self.visited[v]:
                self.low[u] = min(self.low[u], self.tin[v])
            else:
                self.dfs(v, u)
                self.low[u] = min(self.low[u], self.low[v])

                if self.low[v] >= self.tin[u] and p != -1:
                    self.articulation_points.add(u)
                children += 1

        if p == -1 and children > 1:
            self.articulation_points.add(u)

    def find_articulation_points(self):
        for i in range(self.n):
            if not self.visited[i]:
                self.dfs(i)
        return list(self.articulation_points)
