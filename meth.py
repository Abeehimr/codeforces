
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

def mobius_sieve(n):
    """
    Returns a list mobius where mobius[i] is the value of the Möbius function μ(i) for all i in [0, n].
    The Möbius function is defined as:
- μ(n) = 1 if n is a square-free positive integer with an even number of prime factors.
- μ(n) = -1 if n is a square-free positive integer with an odd number of prime factors.
- μ(n) = 0 if n has a squared prime factor.
    """
    mobius = [1] * (n + 1)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i): is_prime[j] = False
            for j in range(i, n + 1, i): mobius[j] *= -1
            for j in range(i*i, n + 1, i*i): mobius[j] = 0
    mobius[0] = 0
    return mobius
