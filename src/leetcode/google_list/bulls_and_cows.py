"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

    The number of "bulls", which are digits in the guess that are in the correct position.
    The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.



1 2 2 3
  |   
3 2 1 1

have a counter for the target and another for the guess

{
3: 1
2: 1
1: 1
}


{
3: 1
2: 0
1: 2
}

count the bulls
    for each bull, remove one from both the counters

count the cows looking at the both counters (iterating on the guess counter)
    decrease one for every match, dont use elements with 0 count on the target


O(n) time complexity where n is the size of the guess/target
O(1) space complexity since counter is limited to 10 items (0 to 9)

In - guess: str, target: str
Out - str



------------
Improving to a single pass


The idea here is to use a single counter, fill it on the go adding 1 to char on target, subtracting for chars on guess. The key is to add to cows when tagert counter < 0 and guess counter > 0.

1 2 2 3

3 2 1 1


1: -1
2: 1
3: -1

when equal
    add to bulls

when they are different 
    if the guess element counter is > 0 we add to cows
    if the target element counter is < 0 we add to cows
    for the element on guess we remove one from counter
    for the element on the target we add one on the counter

O(n) time complexity (but with single pass)
O(1) space



"""
import collections
from typing import Dict


class SolutionOld:
    def getHint(self, target: str, guess: str) -> str:
        target_counter: Dict[str, int] = collections.Counter(target)
        guess_counter: Dict[str, int] = collections.Counter(guess)
        bulls: int = self.find_bulls(target, guess, 
                                     target_counter, guess_counter)
        cows: int = self.find_cows(target_counter, guess_counter)
        return f'{bulls}A{cows}B'

    def find_bulls(self, target: str, guess: str, 
                   target_counter: Dict[str, int], 
                   guess_counter: Dict[str, int]) -> int:
        bulls: int = 0
        for target_char, guess_char in zip(target, guess):
            if target_char != guess_char:
                continue
            bulls += 1
            target_counter[target_char] -= 1
            guess_counter[guess_char] -= 1
        return bulls

    def find_cows(self, target_counter: Dict[str, int], 
                  guess_counter: Dict[str, int]) -> int:
        cows: int = 0
        for guess in guess_counter:
            if guess not in target_counter:
                continue
            cows += min(target_counter[guess], guess_counter[guess])
        return cows
            

# Improved solution

import collections
from typing import Dict


class Solution:
    def getHint(self, target: str, guess: str) -> str:
        counter: Dict[str, int] = collections.defaultdict(int)
        bulls: int = 0
        cows: int = 0
        for target_char, guess_char in zip(target, guess):
            if target_char == guess_char:
                bulls += 1
                continue
            if counter[target_char] < 0:
                cows += 1
            if counter[guess_char] > 0:
                cows += 1
            counter[guess_char] -= 1
            counter[target_char] += 1
        return f'{bulls}A{cows}B'
            
