"""

Find the list of primes up to n

in - number: int

out - List[int] prime numbers

sieve of eratostheles

number = 5

0 1 2 3 4 5
f f t t f t

result
2 3 5
"""
from typing import List, Optional


def find_primes(number: int) -> List[int]:
    """ Finds all primes up to number """
    if number < 2:
        return []
    primes: List[int] = []
    # Initializes all to True, but 0 and 1
    is_prime: List[bool] = [False] * 2 + [True] * (number - 1)
    curr_prime: Optional[int] = 2
    while curr_prime and curr_prime <= number:
        primes.append(curr_prime)
        remove_non_primes(is_prime, curr_prime)
        curr_prime = find_next_prime(is_prime, curr_prime)
    
    return primes


def remove_non_primes(is_prime: List[bool], curr_prime: int) -> None:
    """ Sets false on all multiple of curr prime """
    for i in range(curr_prime * curr_prime, len(is_prime), curr_prime):
        is_prime[i] = False
        
        
def find_next_prime(is_prime: List[bool], curr_prime: int) -> Optional[int]:
    for i in range(curr_prime + 1, len(is_prime)):
        if is_prime[i]:
            return i


print(find_primes(15))
import pdb;pdb.set_trace()
