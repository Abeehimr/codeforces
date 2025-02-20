from sys import stdin
input = stdin.readline

INF = float('inf')
MOD = 1_000_000_007
MOD1 = 998_244_353

def solve(I):
    n, = map( int , input().strip().split() )
    arr = list( map( int , input().strip().split() ) )
    mat = [list(map(int,input().strip().split())) for _ in range(n)]



q = 1
q = int(input().strip())
for i in range(q):
    solve(i+1)