from sys import stdin
input = stdin.readline

INF = float('inf')
MOD = 1_000_000_007
MOD1 = 998_244_353

def solve(I):
    N, = map( int , input().strip().split() )
    arr = list( map( int , input().strip().split() ) )
    mat = [list(map(int,input().strip().split())) for _ in range(N)]



q = 1
for i in range(q):
    solve(i+1)