n = int(input())
adj = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dfs = [(1, 0)]
for v, p in dfs:
    for child in adj[v]:
        if p != child:
            dfs.append((child, v))

# print(dfs)
dp = [None] * (n+1)
ans = 0
for v, p in dfs[::-1]:
    ...