

########## LINEAR SIEVE ############
MX =5_000_001
lsp = list(range(MX))
primes = []
for i in range(2, MX):
    if lsp[i] == i: primes.append(i)
    for p in primes:
        if i * p >= MX: break
        lsp[i * p] = p
        if i % p == 0: break
####################################

