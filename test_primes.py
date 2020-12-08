import primes_tools as pt
from math import sqrt
#from primes_tools import print_primes
from primes_tools import is_prime
#from primes_tools import *         # deprecated

def test_if_is_prime_for_7():    
    assert is_prime(7) == True

def test_if_is_prime_for_6():        
    assert is_prime(6) == False

def test_primes_return_empty_list():        
    assert pt.primes(0) == []

def test_primes_return_short_list():        
    assert pt.primes(3) == [2, 3, 5]

def test_primes_check_last_item():        
    assert pt.primes(97)[-1] == 97

# pip install pytest
# https://pypi.org/project/pip/

# Ctrl+Shift+P - palette
# Configure Tests -> pytest -> root folder
# Discover Tests  