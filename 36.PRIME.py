import math

def find_prime_or_not(n):
    sqrt = int(math.sqrt(n))
    flag = 0
    for i in range(2, sqrt + 1):
        if n % i == 0:
            flag = 1
    if flag == 0:
        return True
    else:
        return False

n = int(input())
prime_or_not = find_prime_or_not(n)
print(prime_or_not)