"""
You are given the following :

    A positive number N
    Heights : A list of heights of N persons standing in a queue
    Infronts : A list of numbers corresponding to each person (P) that gives the number of persons who are taller than P and standing in front of P

You need to return  list of actual order of persons’s height

Consider that heights will be unique

Example

Input : 
Heights: 
5 3 2 6 1 4
0 1 2 0 3 2

    1 
    3

Output : 
actual order is: 5 3 2 1 6 4 

So, you can see that for the person with height 5, there is no one taller than him who is in front of him, and hence Infronts has 0 for him.

For person with height 3, there is 1 person ( Height : 5 ) in front of him who is taller than him.

You can do similar inference for other people in the list.



the key here is to insert on a new array and insert in a manner that you know that every inserted element is smaller then your self. So have the input sorted

That way when you insert, all you have to do is put x empty spaces on your left. that later will be filled by bigger elements

A plain implementation of this will see you counting empty spaces to a O(n^2) time complexity
Another way is to keep track of how many empty spaces you have on the left and binary search it to find the desired num of spaces, but on every uptade it would take O(n)

the solution for this problem is to use segment trees

O(n log n) time complexity n is the size of the input
O(n) space

"""
import collections
from typing import List, Optional, Tuple, Optional


Interval = collections.namedtuple('Interval', 'start end')


# Segment tree of the sum of empty slots
class BIT:

    def __init__(self, size: int) -> None:
        self.tree: List[int] = [0] * (size + 1)

    def update(self, index: int, value: int) -> None:
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def query(self, index: int) -> int:
        result: int = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, nums: List[int], heights: List[int]) -> List[Optional[int]]:
        nums_heights: List[Tuple[int, int]] = list(zip(nums, heights))
        nums_heights.sort()
        result: List[Optional[int]] = [None] * len(nums)
        tree: BIT = BIT(len(nums))
        # Fills the tree of slots
        for index in range(1, len(nums) + 1):
            tree.update(index, 1)
        for num, height in nums_heights:
            index: int = self.find_index(result, height, tree)
            result[index] = num
        return result

    def slow_find_index(self, slots: List[Optional[int]], height: int) -> int:
        count: int = 0
        for index, slot in enumerate(slots):
            if slot is None:
                count += 1
            if count == height + 1:
                return index
        raise ValueError('Index not found')

    def find_index(self, slots: List[Optional[int]], height: int, 
                   tree: BIT) -> int:
        start, end = 1, len(slots)
        index: int = -1
        while start <= end:
            mid: int = (start + end) // 2
            curr: int = tree.query(mid)
            if curr > height + 1:
                end = mid - 1
            elif curr < height + 1:
                start = mid + 1
            else:
                index = mid
                break
        tree.update(index, -1)
        return index - 1

        

    
    
            

