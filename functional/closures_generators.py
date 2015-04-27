# Keeps full series in a list
def fib(n):
    l = [0,1]
    while(len(l) < n):
        l.append(l[-1] + l[-2])
    return l[n-1]

# Only keeps last two values in a list (I assume, Maybe better for very high fib number?)
def fib2(n):
    l = [0,1]
    # take into account list starts with two values with len
    for i in range(len(l), n):
        l.append(l[-1] + l[-2])
        l = l[1:]
    return l[-1]


def fib_memo():
    l = [0,1]
    def fib(n):
        try:
            return l[n-1]
        except IndexError:
            l.append(l[-1] + l[-2])
            return fib(n)
    return fib

fib_closure = fib_memo()
print fib_closure(5)
print fib_closure(300)

