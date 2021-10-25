"""
Shuffle: Write a method to shuffle a deck of cards. It must be a perfect shuffle-in other words, each
of the 52! permutations of the deck has to be equally likely. Assume that you are given a random
number generator which is perfect

In - cards: List[int]
Out - List[int]

"""
import random
import time
from typing import List


def suffle(cards: List[int]) -> List[int]:
    random.seed(time.time())
    shuffle_helper(cards, i=len(cards)-1)
    return cards


def shuffle_helper(cards: List[int], i: int) -> None:
    if i == 0:
        return
    shuffle_helper(cards, i - 1)
    swap_index: int = random.randint(0, i)
    cards[i], cards[swap_index] = cards[swap_index], cards[i]


print(suffle([a for a in range(52)]))
