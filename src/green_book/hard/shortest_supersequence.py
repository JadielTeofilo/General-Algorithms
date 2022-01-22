"""
Shortest Supersequence: You are given two arrays, one shorter (with all distinct elements) and one
longer. Find the shortest subarray in the longer array that contains all the elements in the shorter
array. The items can appear in any order.

1, 5, 9
7, 5, 9, 8, 2, 1, 3, 7, 9, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7

brute force approach
    start from every position and go until you find all elements

In - shorter: List[int], bigger: List[int]
Out - List[int]

better

    have a dictionary with the most recently seen positions
    at each new find of the smaller array, recalculate the size, keep track of the min

    O(s*b) time complexity where s is the size of the smaller and b the bigger
    O(s) space complexity



"""
import collections
import math
from typing import List, Dict, Union, Optional, Set


SubArray = collections.namedtuple('SubArray', 'start end')


def shortest_supersequence(short: List[int], 
                           bigger: List[int]) -> List[int]:
    recent: Dict[int, int] = find_first_occurences(
        bigger, short
    )
    min_size: Union[int, float] = math.inf
    sub_array: Optional[SubArray] = None
    for i, number in enumerate(bigger):
        if number in recent:  # If its part of the short list
            recent[number] = i  # Updates the cache
        new_distance: int = get_distance(recent)
        if new_distance < min_size:
            sub_array = SubArray(i - new_distance, i)
            min_size = new_distance
    if sub_array is not None:
        return bigger[sub_array.start:sub_array.end + 1]
    raise ValueError('Short is not a subarray of bigger')


def find_first_occurences(
    bigger: List[int], short: List[int]
) -> Dict[int, int]:
    """
        Sets the recents cache with the first occurrence 
        of each number on short and returns it
    """
    targets: Set[int] = set(short)
    recent: Dict[int, int] = {}
    for index, number in enumerate(bigger):
        if not targets:
            break
        if number not in targets:
            continue
        targets.remove(number)
        recent[number] = index
    return recent
   

def get_distance(recent: Dict[int, int]) -> int:
    max_number: int = max(recent.values())
    min_number: int = min(recent.values())
    return max_number - min_number


short = [1, 5, 9]
bigger = [7, 5, 9, 8, 2, 1, 3, 7, 9, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
print(shortest_supersequence(short, bigger))
