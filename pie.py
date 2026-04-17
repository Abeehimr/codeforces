from math import gcd
def PIE(n, l):
    """Returns the count of numbers in [1, n] that are divisible by at least one of the numbers in list l.
    """
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

from math import comb, gcd
def GPIE(arr,k, l):
    """
    Returns the count of numbers in [1, l] that are divisible by at exactly k of the numbers in list arr.
    """
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