"""
Given an array of integers A.  There is a sliding window of size B which 

is moving from the very left of the array to the very right. 

You can only see the w numbers in the window. Each time the sliding window moves 

rightwards by one position. You have to find the maximum for each window. 

The following example will give you more clarity.

The array A is [1 3 -1 -3 5 3 6 7], and B is 3.
Window position 	Max
———————————- 	————————-
[1  3  -1] -3  5  3  6  7 	3
3
1 [3  -1  -3] 5  3  6  7 	3

1  3 [-1  -3  5] 3  6  7 	5
1  3  -1 [-3  5  3] 6  7 	5
1  3  -1  -3 [5  3  6] 7 	6
1  3  -1  -3  5 [3  6  7] 	7

Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].

Note: If B > length of the array, return 1 element with the max of the array.





In - nums: List[int]
Out - max_values: List[int]


The brute force is to calculate the max for each new window

get the curr max, if invalid pop it

setup the first window (itearate on the members inserting on maxheap/hash)

Iterate on the new indexes, we add it at each step (just add to the maxheap)
    then we remove the old element index - size, (mark as invalid)

But we are redoing work, we can have a heap with (negated value, value, valid?) a hash poiting to the HeapValue



O(nlogn) time complexity amortized where n the size of nums
O(b) space where b is the size of the window


"""
from typing import List


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, nums: List[int], size: int) -> List[int]:
        heap: List[HeapValue] = []  # TODO
        cache: Dict[int, HeapValue] = {}  # Keyed by index
        for start in range(len(nums)):
            end: int = start + size - 1
            curr


            
        

