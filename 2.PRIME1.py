import math
import numpy as np

def find_primes(high):
    primes = [True for i in range(high + 1)]
    primes[0] = False
    primes[1] = False
    num = 2
    while num <= high:
        if primes[num]:
            for i in range(num * num, high + 1, num):
                primes[i] = False
        num += 1

    list_primes = [i for i in range(high + 1) if primes[i]]
    return list_primes

def filter_primes(low, high):
    primes_seed = find_primes(int(math.sqrt(high)))
    low = max(low, 2)
    is_prime = {x: True for x in range(low, high + 1)}
    for prime in primes_seed:
        first_divisor = max(math.ceil(low / prime) * prime, prime * prime)
        for num in range(first_divisor, high + 1, prime):
            is_prime[num] = False
        
    list_primes = [k for k, v in is_prime.items() if v]
    return list_primes

t = int(input())
for _ in range(t):
    input_str = input()
    low, high = [int(x) for x in input_str.split(' ')]
    list_primes = filter_primes(low, high)
    for prime in list_primes:
        print(prime)
    print()