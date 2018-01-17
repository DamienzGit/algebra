from sympy.ntheory import isprime, factorint

def phi(n):
    if isprime(n):
        return n-1
    factors = factorint(n)
    prod = 1
    for factor, exp in factors.items():
        prod *= factor**(exp-1) * (factor - 1)
    return prod

