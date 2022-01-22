"""
Rand7 from RandS: Implement a method rand7() given randS(). That is, given a method that
generates a random number between 0 and 4 (inclusive), write a method that generates a random
number between 0 and 6 (inclusive).

def rand5():
    return random.randint(1, 5)

call twice:
2 4, adding gives 6
4 2
0 1
1 0

5 * 5 = 25
% 7


"""
from typing import Dict
import time
import random

BITS_OF_SEVEN = 3


def rand5() -> int: 
    random.seed(time.time())
    return random.randint(1,4)


def rand7() -> int:
    while True:
        rand25: int = 5 * rand5() + rand5()
        if rand25 > 20:
            continue
        return rand25 % 7

print(rand7())
