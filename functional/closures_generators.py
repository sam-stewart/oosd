# Keeps full series in a list
def fib(n):
    l = [0,1]
    while(len(l) < n):
        l.append(l[-1] + l[-2])
    return l[n-1]

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

print fib3(5)
