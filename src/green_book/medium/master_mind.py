"""
Master Mind: The Game of Master Mind is played as follows:
The computer has four slots, and each slot will contain a ball that is red (R), yellow (Y), green (G) or
blue (B). For example, the computer might have RGGB (Slot #1 is red, Slots #2 and #3 are green, Slot
#4 is blue).
You, the user, are trying to guess the solution. You might, for example, guess YRGB.
When you guess the correct color for the correct slot, you get a "hit:' If you guess a color that exists
but is in the wrong slot, you get a "pseudo-hit:' Note that a slot that is a hit can never count as a
pseudo-hit.
For example, if the actual solution is RGBY and you guess GGRR, you have one hit and one pseudo-
hit.
Write a method that, given a guess and a solution, returns the number of hits and pseudo-hits

Should we think of a generic approach concerning the size of the guess

In - guess: Balls, solution: Balls
Out - Hits

validate size of inputs

RGBY   GGRR

1 - hits, counter


O(n) space and time, where n is the size of the input
"""
import enum
import collections
from typing import List, Dict


class Color(enum.Enum):
    red = 1
    yellow = 2
    green = 3
    blue = 4


Ball = collections.namedtuple('Ball', 'color')
_Balls = List[Ball]
Hits = collections.namedtuple('Hits', 'normal pseudo')
Counter = Dict[Color, int]


def master_mind(guess: _Balls, solution: _Balls) -> Hits:
    # TODO check sizes of inputs
    solution_remainder_counter: Counter = collections.defaultdict(int)
    normal_hits: int = get_normal_hits(
        guess, solution, solution_remainder_counter
    )
    pseudo_hits: int = get_pseudo_hits(
        guess, solution, solution_remainder_counter
    )
    return Hits(normal_hits, pseudo_hits)


def get_normal_hits(
    guess: _Balls, solution: _Balls, 
    solution_remainder_counter: Counter
) -> int:
    """ Finds the regular hits and updates the counter """
    result: int = 0
    for i in range(len(guess)):
        if guess[i].color == solution[i].color:
            result += 1
        else:
            solution_remainder_counter[solution[i].color] += 1
    return result


def get_pseudo_hits(
    guess: _Balls, solution: _Balls, 
    solution_remainder_counter: Counter) -> int:
    """ Finds and returns the pseudo hits """
    result: int = 0
    for i in range(len(guess)):
        if guess[i].color == solution[i].color:
            continue
        if solution_remainder_counter[guess[i].color] > 0:
            result += 1
            solution_remainder_counter[guess[i].color] -= 1
    return result



print(master_mind(
        [Ball(Color.red), Ball(Color.green), Ball(Color.red), Ball(Color.yellow)],
        [Ball(Color.green), Ball(Color.yellow), Ball(Color.red), Ball(Color.green)],
        ))

    
print(master_mind(
        [Ball(Color.red), Ball(Color.green), Ball(Color.red), Ball(Color.yellow)],
        [Ball(Color.yellow), Ball(Color.yellow), Ball(Color.blue), Ball(Color.green)],
        ))


