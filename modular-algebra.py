from sympy.ntheory import isprime, factorint


def phi(n):
    if isprime(n): return n-1
    factors, prod = factorint(n), 1
    for factor, exp in factors.items(): prod *= factor**(exp-1) * (factor - 1)
    return prod

def egcd(a, b):
    if a == 0: return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def _modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1: raise Exception('No modular inverse')
    return x%m

def invert(n, mod): return _modinv(n, mod)


