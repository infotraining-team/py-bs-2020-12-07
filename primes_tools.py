## TODO
## create function that prints primes 2-limit
## but use help function
## is_prime(n) -> True | False

def print_primes(limit):
    for n in range(2, limit+1):
        if is_prime(n):
            print(n)

def primes(limit):
    return []

def is_prime(num):
    for div in range(2, num):
        if num % div == 0:
            return False
    return True

print("Module is loading...")

if __name__ == "__main__":    
    print_primes(100)

