"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

In - numbers: List[int]
Out - int


3 5 4 1 9 2

3 2 
3 4
3 5
5 2 


1 2 3 4 5 9
3 5 0 2 1 4
 

O(nlogn) time complexity where n is the size of the list
O(n) space complexity 


"""
import collections
import math
from typing import List, Union


Node = collections.namedtuple('Node', 'value index')


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, numbers: List[int]) -> int:
        if not numbers:
            return 0
        nodes: List[Node] = [Node(num, i) 
                             for i, num in enumerate(numbers)]
        nodes.sort()
        return self.find_longest_distance(nodes)

    def find_longest_distance(self, nodes: List[Node]) -> int:
        min_value: Union[float, int] = math.inf
        result: Union[float, int] = -math.inf
        for _, index in nodes:
            min_value = min(min_value, index)
            result = max(result, index - min_value)
        # Sets to zero in the case where there is 
        # no distance to be had
        result = result if result > 0 else 0
        return int(result)


