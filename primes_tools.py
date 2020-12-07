## TODO
## create function that prints primes 2-limit
## but use help function
## is_prime(n) -> True | False

def print_primes(limit):
    for n in range(2, limit+1):
        if is_prime(n):
            print(n)

def is_prime(num):
    for div in range(2, num):
        if num % div == 0:
            return False
    return True

print("Testing")
assert is_prime(7) == True
assert is_prime(6) == False
    
print_primes(100)
