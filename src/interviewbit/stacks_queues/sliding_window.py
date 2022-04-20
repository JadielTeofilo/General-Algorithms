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

-------------
Official Solution:

The double-ended queue is the perfect data structure for this problem. It supports insertion/deletion from the front and back. The trick is to find a way such that the largest element in the window would always appear in the front of the queue. How would you maintain this requirement as you push and pop elements in and out of the queue?

You might notice that there are some redundant elements in the queue that we shouldn’t even consider about. For example, if the current queue has the elements: [10 5 3], and a new element in the window has the element 11. Now, we could have emptied the queue without considering elements 10, 5, and 3, and insert only element 11 into the queue.

A natural way most people would think is to try to maintain the queue size the same as the window’s size. Try to break away from this thought and try to think outside of the box. Removing redundant elements and storing only elements that need to be considered in the queue is the key to achieve the efficient O(n) solution.
-------------------------------



In - nums: List[int]
Out - max_values: List[int]


We only care about the first and last elements of window, so we use a queue and we keep a right and a left pointers

A monotonic queue allows us to only keep the bigger elements in front, skipping smaller elements that are to the left. That is the key here, smaller elements on the left dont matter. 

we add the right element to the monotonic queue
we remove the left element if it is on the top of the queue
 
[1  3  -1] -3  5  3  6  7 	3

[3 -1] 

neetcode link https://www.youtube.com/watch?v=DfljaUwZsOk

O(n) time complexity amortized where n the size of nums
O(n/b) space where b is the size of the window


"""
import collections
from typing import List, Deque


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, nums: List[int], size: int) -> List[int]:
        deque: Deque[int] = collections.deque()
        left, right = 0, 0
        result: List[int] = []
        while right < len(nums):
            while deque and nums[right] > nums[deque[-1]]:
                deque.pop()
            deque.append(right)
            if right + 1 >= size:
                result.append(nums[deque[0]])
                left += 1
            if deque and left > deque[0]:
                deque.popleft()
            right += 1
        return result
            
        

            
        

