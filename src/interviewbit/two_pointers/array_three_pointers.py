"""
You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :

max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.

Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))


_
6 7 
   _
-3 5
_



we want to find the values that are the closest 

we start at the index 0 for all arrays
we take the array with smallest value that still hasnt reached the end and increase its index
idea is to make it get closer to the values on the other lists
at each step we update the result

handle empty lists

O(n) time complexity where n is the size of the biggest list
O(1) space


"""
import dataclasses
import math
from typing import List, Dict, Tuple, Optional, Union



class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, left: List[int], mid: List[int], 
                 right: List[int]) -> int:
        i, j, k = 0, 0, 0
        min_distance: Union[int, float] = math.inf
        while self.there_are_positions_to_move(
            left, i, mid, j, right, k
        ):
            i, j, k = self.move_position(left, i, mid, j, right, k)
            min_distance = min(
                min_distance, 
                max(abs(left[i] - mid[j]), abs(mid[j] - right[k]), 
                    abs(right[k] - left[i]))
            )
        if min_distance == math.inf:
            raise ValueError('Empty input')
        return min_distance

    def there_are_positions_to_move(
        self, left: List[int], i: int, mid: List[int], 
        j: int, right: List[int], k: int
    ) -> bool:
        # Finds out when there are at least two positions to move
        return ((int(i < len(left)) + 
                 int(j < len(mid)) + 
                 int(k < len(right))) >= 2)

    def move_position(
        self, left: List[int], i: int, mid: List[int], 
        j: int, right: List[int], k: int
    ) -> Tuple[int, int, int]:

        @dataclasses.dataclass
        class Option:
            numbers: List[int]
            index: int

        options: List[Option] = [Option(left, i), 
                                 Option(mid, j), 
                                 Option(right, k)]
        result: Dict[int, Option] = {index: option 
                                     for index, option in enumerate(options)}
        options.sort(key=lambda numbers, index: numbers[index])
        for i, option in enumerate(options):
            if option.index >= len(option.numbers):
                continue
            options[i].index += 1
            break
        return (result[0].index, result[1].index, result[2].index)
        
        
 
