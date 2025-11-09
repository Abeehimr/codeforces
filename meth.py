def gcd(x,y):
    while x: x,y = y%x,x
    return y

def lcm(x,y):
    return x*y//gcd(x,y)


def ceil(n):
    v = int(n)
    if v < n: v += 1
    return v

def msb(n):
    if n == 0: return -1
    out = 0
    while n:
        n >>= 1
        out += 1
    return out

def getcount(N, k):
    """count number from 0 to N where kth bit is set"""
    bit_length = 1 << k  # Equivalent to 2^k
    cycle_length = bit_length<<1  # Equivalent to 2^(k+1)
    # Full cycles of 2^(k+1) within the range [0, N]
    full_cycles = (N + 1) // cycle_length
    # Remaining numbers after the full cycles
    remainder = (N + 1) % cycle_length
    # Count of numbers where the k-th bit is set
    count = full_cycles * bit_length + max(0, remainder - bit_length)
    return count

def divceil(a,b):
    
    return (a+b-1)//b

def factors(n):
    i = 1
    while i*i <= n:
        if n%i == 0:
            yield i
            if i*i < n:yield n//i
        i += 1

mx = 2*(10**5) + 1
p=  [i for i in range(mx)]
i = 2
while i*i < mx:
    if p[i] == i:
        for k in range(i*i,mx,i):
            if p[k] == k:
                p[k] = i
    i += 1

lp = [i for i in range(2,mx) if p[i] == i]

##############
N =5_000_001
is_prime = [True] * N
primes = []
is_prime[0] = is_prime[1] = False
for i in range(2, N):
    if is_prime[i]:  
        primes.append(i)
    for p in primes:
        if i * p >= N:
            break
        is_prime[i * p] = False
        if i % p == 0:
            break  # Ensures each number is marked only once by its smallest prime
#############


MOD = 10**9 + 7
N = 1001
fac = [i for i in range(N)]
fac[0] = 1
for i in range(2,N):
    fac[i] = fac[i]*fac[i-1]%MOD

inv = [1]*N
inv[N-1] = pow(fac[N-1],MOD-2,MOD)
for i in range(N-2,0,-1):
    inv[i] = (i+1)*inv[i+1]%MOD


def MUL(A,B):
    a , b , c = len(A) , len(A[0]) , len(B[0])
    out = [[0]*c for _ in range(a)]
    for x in range(a):
        for y in range(c):
            for z in range(b):
                out[x][y] += A[x][z]*B[z][y]
    return out


def po(base,power):
    out = 1
    while power > 0:
        if power&1:
            out *= base
        power >>= 1
        base *= base
    return out

def PIE(n, l):
    ans = 0
    for i in range(1, 1 << len(l)):
        bits = bin(i).count('1')
        lcm = 1
        for j in range(len(l)):
            if i & (1 << j):
                lcm = lcm * l[j] // gcd(lcm, l[j])
        if bits % 2 == 1:
            ans += n // lcm
        else:
            ans -= n // lcm
    return ans

from math import comb
def GPIE(arr,k, l):
    N = len(arr)
    out = 0
    for msk in range(1, 1 << N):
        r = msk.bit_count()
        if r < k:
            continue
        lc = 1
        for j in range(N):
            if msk & (1 << j):
                lc = lc // gcd(lc, arr[j]) * arr[j]
            
        if (r - k)&1:
            out -= (l//lc)*comb(r,k)
        else:
            out += (l//lc)*comb(r,k)
    return out


def nextPermutation(nums):
    i = len(nums) - 2
    while(nums[i] >= nums[i+1] and i > -1):
        i -= 1
    if i == -1:
        nums.reverse()
        return
    j = len(nums) - 1
    while (nums[i] >= nums[j] and i < j):
        j-= 1
    nums[i],nums[j] = nums[j],nums[i]
    nums[i+1:] = nums[i+1:][::-1]

def compute_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result