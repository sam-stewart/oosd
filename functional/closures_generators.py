from math import sqrt

# Formula from wolfram alpha
def fib_wolfram(n):
    return int(((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5)))

# Recursion play. Return nth fibonacci number
def fib_recurse(n, a=0, b=1, c=2):
    if c > n:
        return b
    return fib_recurse(n, b, b+a, c+1)

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
    for i in range (2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

