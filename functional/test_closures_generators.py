import unittest
from timeit import timeit
from closures_generators import *

class TestClosures(unittest.TestCase):

    def setUp(self):
        # tenth fibonacci number
        self.fib10 = 55
        # primes 0 to 20
        self.primes = [1,2,3,5,7,11,13,17,19]

    def test_fib_wolfram(self):
        self.assertEquals(fib_wolfram(10), self.fib10)

    def test_fib_recurse(self):
        self.assertEquals(fib_recurse(10), self.fib10)

    def test_fib_memo(self):
        self.f = fib_memo()
        self.assertEquals(self.f(10), self.fib10)

    def test_get_primes(self):
        self.f = get_primes(20)
        self.assertItemsEqual([i for i in self.f], self.primes)

    def test_fib_exec(self):
        print(timeit("fib_wolfram(10)", setup="from closures_generators import fib_wolfram"))
        print(timeit("fib_recurse(10)", setup="from closures_generators import fib_recurse"))
        print(timeit("fib(10)", setup="from closures_generators import fib_memo \nfib = fib_memo()"))

if __name__ == '__main__':
    unittest.main()

