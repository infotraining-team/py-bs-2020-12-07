## print the primes in range 2-100
## prime 

for number in range(2, 101):
    # detect primes
    is_prime = True
    for div in range(2, number):
        if number % div == 0:
            is_prime = False
            break
    if is_prime:
        print(number)

print("-"*40)

for number in range(2, 101):    
    for div in range(2, number):
        if number % div == 0:            
            break
    else:
        print(number)

# print("-"*40)
# print(" testing 7")
# print( 7 % 2 )
# print( 7 % 3 )
# print( 7 % 4 )
# print( 7 % 5 )
# print( 7 % 6 )
# print(" testing 6")
# print( 6 % 2 )
# print( 6 % 3 )
# print( 6 % 4 )
# print( 6 % 5 )
