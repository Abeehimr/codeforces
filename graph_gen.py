import random

# n m weighted adjs
# connected
import random
MX = 10**1

def generate_connected_graph(n, extra_edges=0):
    """
    Generates a connected undirected graph with n nodes.
    Returns a list of edges as (u, v) tuples.
    """
    if n <= 1:
        return []

    edges = []
    parent = list(range(n))
    random.shuffle(parent)

    # Step 1: Create a spanning tree to ensure connectivity
    for i in range(1, n):
        u = parent[i]
        v = parent[random.randint(0, i - 1)]
        if u != v:
            edges.append((min(u, v) + 1, max(u, v) + 1,random.randint(1, MX)))

    # Step 2: Add extra edges randomly (optional)
    added = set(edges)
    attempts = 0
    while len(edges) < n - 1 + extra_edges and attempts < 5 * extra_edges:
        u, v = random.sample(range(n), 2)
        edge = (min(u, v) + 1, max(u, v) + 1,random.randint(1, MX))
        if edge not in added:
            edges.append(edge)
            added.add(edge)
        attempts += 1

    return edges


N = random.randint(2, 1000)
extra = random.randint(0, 1000)
edges = generate_connected_graph(N, extra)
print(N, len(edges))
for u, v, w in edges:
    print(u, v, w)


# for u, v, w in edges:
#     adj[u-1].append(v-1)
#     adj[v-1].append(u-1)

#     par = [-1] * N
    # st = [(0, -1)]
    # while st:
    #     u, p = st.pop()
    #     par[u] = p
    #     for v in adj[u]:
    #         if v != p:
    #             st.append((v, u))

    # for i in range(N):
    #     print(i+1, len(adj[i]) - int(par[i] != -1), *[u + 1 for u in adj[i] if u != par[i]])