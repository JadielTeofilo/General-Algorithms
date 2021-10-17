"""
Sum Swap: Given two arrays of integers, find a pair of values (one value from each array) that you
can swap to give the two arrays the same sum.

In - first: List[int] second: List[int]
Out - Pair

Input:{4 1 2 1 1 2} and {3 6 3 3}
Output: {1 3}

4 1 2 1 1 2 = 11
3 6 3 3 = 15



4 3 2 1 1 2 = 13
3 6 3 1 = 13


Am i garanteed to have it?
No

What if they already have the same value
No element is required to change, return none

O(n) time where n is the size of the bigger array


"""
import collections
from typing import List, Optional, Set


Pair = collections.namedtuple('Pair', 'first_val second_val')


def sum_swap(first: List[int], second: List[int]) -> Optional[Pair]:
    """ 3 6 3 3 _______  4 1 2 1 1 2 """
    # TODO check for oempty inpuyt
    first_sum: int = sum(first)  # 15
    second_sum: int = sum(second)  # 11
    if first_sum < second_sum:
        # Have the first always be the biggest
        return sum_swap(second, first)
    if first_sum == second_sum:
        return None
    first_unique_nums: Set[int] = set(first)  # 3 6
    second_unique_nums: Set[int] = set(second)  # 4 1 2
    for second_num in second_unique_nums:  # 1
        # Finds the expected value on first given the curr second num
        target: float = (second_num + first_sum - second_sum) / 2
        if int(target) == target and int(target) in first_unique_nums:
            return Pair(int(target), second_num)
    return None


print(sum_swap([4,1,2,1,1,2], [3,6,3,3]))


