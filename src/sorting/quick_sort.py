"""

Quick sort using swaps

The recursion works with the following pattern:

quicksort(left)
quicksort(right)

The swaps works like so:

    Have two pointers each on either side, bring them in until you find an element that must be swaped

"""
from typing import List
import unittest


def quicksort(numbers: List[int]) -> List[int]:
    quicksort_helper(numbers, start=0, end=len(numbers) - 1)
    return numbers


def quicksort_helper(numbers: List[int], 
                     start: int, end: int) -> None:
    if start >= end:
        return
    pivot_index: int = (start + end) // 2
    pivot_index = partition(numbers, pivot_index, start, end)
    quicksort_helper(numbers, start, pivot_index - 1)  # sorts left
    quicksort_helper(numbers, pivot_index,  end)  # sorts right


def partition(numbers: List[int], pivot_index: int, left, right) -> int:
    pivot: int = numbers[pivot_index]
    while left <= right:
        
        while numbers[left] < pivot:
            left += 1
        
        while numbers[right] > pivot:
            right -= 1
        
        if left <= right:
            # Swap values
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1
    
    return left


class Test(unittest.TestCase):
    
    def test_sorting(self):
        """ Should sort the input list """
        target: List[int] = [3,2,7,3,8,1,34,65,21,2,3,4,5,6,3]
        expected: List[int] = [1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 21, 34, 65]
        quicksort(target)
        self.assertEquals(target, expected)
        

if __name__ == '__main__':
    unittest.main()
