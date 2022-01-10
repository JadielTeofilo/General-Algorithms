"""
Given an integer array A of size N consisting of unique integers from 1 to N. You can swap any two integers atmost B times.

Return the largest lexicographical value array that can be created by executing atmost B swaps.

In - numbers: List[int], swaps
Out - List[int]


1 9 2 3 0
9 1 2 3 0

9 1 2
9 2 1

2 3 1
3 2 1

build a max heap (keep index and value) from copy of list
pop and compare with start of list, if equal go to next element and pop again
if diff swap elements subract from swaps and continue

O(slog(n)) time complexity where s is the swaps and n is the size of nums
O(n) space complexity

"""
import collections
import heapq
from typing import List, Dict


Value = collections.namedtuple('Value', 'inverted number index')


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, numbers: List[int], swaps: int) -> List[int]:
        heap: List[Value] = self.build_heap(numbers)
        index: int = 0
        updated_index: Dict[int, int] = {}
        # [3, 2, 4, 1, 5]
        # [5, 4, 3, 2, 1]
        #  5 4 3 1 2
        while heap and swaps > 0:
            current: Value = heapq.heappop(heap)
            if current.number != numbers[index]:
                swaps -= 1
                swap_index = self.get_swap_index(current, updated_index, index)
                numbers[index], numbers[swap_index] = numbers[swap_index], numbers[index]
            index += 1
        return numbers

    def build_heap(self, numbers: List[int]) -> List[Value]:
        heap: List[Value] = [Value(-number, number, index) 
                             for index, number in enumerate(numbers)]
        heapq.heapify(heap)
        return heap

    def get_swap_index(self, current: Value, 
                       updated_index: Dict[int, int],
                       new_index: int) -> int:
        swap_index: int = updated_index.get(current.number, current.index)
        updated_index[current.number] = new_index
        return swap_index



