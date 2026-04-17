MOD = 10**9 + 7
MX = 1_000_001
FAC = [i for i in range(MX)]
FAC[0] = 1
for i in range(2,MX): FAC[i] = FAC[i]*FAC[i-1]%MOD
INV = [1]*MX
INV[MX-1] = pow(FAC[MX-1],MOD-2,MOD)
for i in range(MX-2,0,-1): INV[i] = (i+1)*INV[i+1]%MOD

def nCr(n,r):
    if r > n or r < 0: return 0
    return FAC[n]*INV[r]%MOD*INV[n-r]%MOD

def nPr(n,r):
    if r > n or r < 0: return 0
    return FAC[n]*INV[n-r]%MOD

def nHr(n,r):
    if n == 0 and r == 0: return 1
    if n <= 0 or r < 0: return 0
    return nCr(n+r-1,r)
    