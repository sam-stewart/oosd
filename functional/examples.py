# examples from 8.2 slide

def fact_builder():
    memo = [1, 1]
    def f(n):
        try:
            return memo[n]
        except IndexError:
            result = n * f(n-1)
            memo[n] = result
            return result
        return f

def counter(n):
    count = 0
    while count < n:
        yield count
        count += 1

# Generator function from jeffknupp
import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) +1), 2):
            if number % current == 0:
                return False
        return True
    return False

# list compre
def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve_number_10():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 200000:
            total += next_prime
        else:
            print(total)
            return
