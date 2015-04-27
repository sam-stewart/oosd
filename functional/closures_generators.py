from math import sqrt

# Formula from wolfram alpha
def fib_cheat(n):
    return ((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5))

# Recursion play.
def fib(n, a=0, b=1, c=0):
    if c >= n:
        return a
    return fib(n, b, b+a, c+1)

def fib_memo():
    l = [0,1]
    def fib(n):
        try:
            return l[n]
        except IndexError:
            l.append(l[-1] + l[-2])
            return fib(n)
    return fib

fib_closure = fib_memo()

print fib_closure(5)
print fib(5)
