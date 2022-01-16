"""
Problem Description

Given a stream of numbers A. On arrival of each number, you need to increase its first occurence by 1 and include this in the stream.

Return the final stream of numbers.

In - numbers: List[int]
Out - List[int]

iterating on numbers
build an output list

[1, 2, 1, 1]
[2, 2, 2, 1]

cache that has the key be the number and the value be the place of first ocurrence

{
    1: [0]
    2: [0, 1]
}
Check against the cache, if there, 
    pop from heap, update the result on that position
    update the cache, of number + 1 and number, just add to the heap
if not add it
resturn result


O(n) space complexity where n is the size of numbers
O(nlogn) time complexity n the size of numbers
"""
import collections
import heapq
from typing import List, Dict


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, numbers: List[int]) -> List[int]:
        if not numbers:
            return numbers
        result: List[int] = []
        cache: Dict[int, List[int]] = collections.defaultdict(list)
        """
        3 1 1 2 2
        
        1: 2
        2: 3 4
        3: 0 1

        3 3 1 2 2

        
        """
        for index, number in enumerate(numbers):
            if number not in cache:
                heapq.heappush(cache[number], index)
            else:
                first_occurr: int = heapq.heappop(cache[number])
                result[first_occurr] += 1
                # Updates the cache
                heapq.heappush(cache[number + 1], first_occurr)
                heapq.heappush(cache[number], index)
            result.append(number)
        return result

