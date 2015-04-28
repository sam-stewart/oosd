from math import sqrt

# Formula from wolfram alpha
def fib_wolfram(n):
    return ((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5))

# Recursion play. Return nth fibonacci number
def fib(n, a=0, b=1, c=2):
    if c > n:
        return b
    return fib(n, b, b+a, c+1)

# Memoisation and recursion, return nth fibonacci number.
# Maintain a list this time, speed up future lookups
def fib_memo():
    l = [0,1]
    def fib(n):
        try:
            return l[n]
        except IndexError:
            l.append(l[-1] + l[-2])
            return fib(n)
    return fib

# Tom's prime implementation - returns primes up to N
def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n, i)}
        p = {x for x in range(2, n) if x not in no_p}
        return p

# Re-implement prime as generator
def get_primes(n):
    for i in range(0, n):
        if is_prime(i):
            yield i

def is_prime(n):
    if n == 0:
        return False
    if n == 1:
        return True
    for i in range (2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True

prime_gen = get_primes(20)

for i in prime_gen:
    print i





