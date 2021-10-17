"""
Pairs with Sum: Design an algorithm to find all pairs of integers within an array which sum to a
specified value.

In - numbers: List[int], target: int
Out - List[Pair]

build set with values that will reach target from the nums

2 5 6 8 2 3 6 1

target = 6 

{4: 2, 1: 5 6: 0}




Want the index or the number?
number

are there duplicates?
yes just return one ocurr

"""
import collections
from typing import List, Dict


Pair = collections.namedtuple('Pair', 'left right')


def pairs_with_sum(numbers: List[int], target: int) -> List[Pair]:
    cache: Dict[int, int] = {}
    result: List[Pair] = []
    for number in numbers:
        if number in cache:
            result.append(Pair(number, cache[number]))
            cache.pop(number)
        cache[target - number] = number
    return result


print(pairs_with_sum([2,5,7,3,4,0,4], 7))
import pdb;pdb.set_trace()

    
