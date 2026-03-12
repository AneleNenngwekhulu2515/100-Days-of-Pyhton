#prime number checker

def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def is_prime(num):
    factors = find_factors(num)
    if len(factors)==2:
        return True
    else:
        return False
print(find_factors(73))
print(is_prime(73))

print(find_factors(75))
print(is_prime(75))

