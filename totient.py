def phi(n: int) -> int:
    """
    Returns the count of integers in [1, n] that are coprime to n."""
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

def phi_sieve(n):
    """Returns a list phi where phi[i] is the count of integers in [1, i] that are coprime to i."""
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi