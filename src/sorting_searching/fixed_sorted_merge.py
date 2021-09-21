"""
Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.

In first: List[int], second: List[int]


[2,3,7,9, , , , ]
[3,4,6,8]



O(n) time n being the size of the bigger string
O(1) space

"""
from typing import List, Optional


def sorted_merge(first: List[Optional[int]], second: List[int]) -> None:
    """ Merges sorted list inplace on the first 
        one, given it has enought space 
    """
    if len(first) < len(second): 
        raise ValueError('The first list must fit second')
    if not first:
        return
    target: int = len(first) - 1  # Index of the insertions
    first_index: int = find_end_of_integers(first)
    second_index: int = len(second) - 1
    while first_index >= 0 and second_index >= 0:
        if first[first_index] > second[second_index]:
            first[target] = first[first_index]
            first_index -= 1
        else:
            first[target] = second[second_index]
            second_index -= 1
        target -= 1
    
    # Stops if the second is the one that 
    # finished first, since the first's 
    # elements are already there
    if second_index < 0:
        return
    
    fill_remaining(first, second, second_index, target)
    
    
def find_end_of_integers(numbers: List[Optional[int]]) -> int:
    for i, number in enumerate(numbers):
        if number is None:
            return i - 1
    return - 1

        
def fill_remaining(first: List[Optional[int]], second: List[int], 
                   second_index: int, target: int) -> None:
    while second_index >= 0:
        first[target] = second[second_index]
        second_index -= 1
        target -= 1
        
        
first = [1,4,6,7,None, None,None, None]
second = [2,3,4,5]
print(first)
sorted_merge(first, second)
print(first)
import pdb;pdb.set_trace()
