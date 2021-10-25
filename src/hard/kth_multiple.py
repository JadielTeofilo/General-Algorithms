"""
Kth Multiple: Design an algorithm to find the kth number such that the only prime factors are 3,5,and 7. Note that 3,5, and 7 do not have to be factors, but it should not have any other prime factors.For example, the first several multiples would be (in order) 1,3,5,7,9,15,21.

brute force

go on each number and check what are its factors, stop on the kth


[3 5 7]


3^0 * 5^0 * 7^0 1
3^1 * 5^0 * 7^0 3
3^0 * 5^1 * 7^0 5
3^0 * 5^0 * 7^1 7
3^2 * 5^0 * 7^0 9
3^1 * 5^1 * 7^0 15
3^1 * 5^0 * 7^1 21
3^0 * 5^2 * 7^1 25


000
111





"""
import math
from typing import List, Set


def kth_multiple(kth: int) -> int:
    if kth <= 0:
        raise ValueError('Kth has to be at least 1')
    primes: List[int] = [3, 5, 7]
    multiples: List[int] = [1]
    number: int = 1
    while kth > 1:
        kth -= 1
        number = generate_valid_multiple(primes, multiples)
    return number


def generate_valid_multiple(primes: List[int], 
                            multiples: List[int]) -> int:
    min_: Union[int, float] = math.inf
    for prime in primes:
        min_ = min(generate_from_prime(prime, multiples), min_)
    multiples.append(int(min_))
    return int(min_)


def generate_from_prime(prime: int, multiples: List[int]) -> int:
    if not multiples:
        raise ValueError('There needs to be at least one multiple')
    visited: Set[int] = set(multiples)
    for multiple in multiples:
        new_multiple: int = prime * multiple
        if new_multiple not in visited:
            return new_multiple

for i in range(1, 25):
    print(kth_multiple(i))

