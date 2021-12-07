"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Example :

Input : [1, 10, 5]
Output : 5

Return 0 if the array contains less than 2 elements.

    You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.
    You may also assume that the difference will not overflow.


5 1 8  9  10 12  2
5 6 14 23 33 45 47

1 2 5 8 9 10 12

get min and max
build buckets the size of min_gap
min_gap is (max - min)//N-1


In - numbers: List[int]
Out - int


"""
import dataclasses
from typing import List, Set, Optional


@dataclasses.dataclass
class Bucket:
	max_number: Optional[int] = None
	min_number: Optional[int] = None


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maximumGap(self, numbers: List[int]) -> int:
		if max(numbers) - min(numbers) < 2:
			return 0
		buckets: List[Bucket] = self.fill_buckets(numbers)
		max_gap: int = 0
		last: Bucket = buckets[0]
		for bucket in buckets[1:]:
			if bucket.min_number is None:
				continue
			if last.max_number is not None:
				max_gap = max(max_gap, bucket.min_number - last.max_number)
			last = bucket
		return max_gap
		  
	def fill_buckets(self, numbers: List[int]) -> List[Bucket]:
		max_: int = max(numbers) 
		min_: int = min(numbers)
		min_gap: int = (max_ - min_) // (len(numbers) - 1) 
		buckets: List[Bucket] = [Bucket() for _ in range(len(numbers)//min_gap)]
		for number in numbers:
			index: int = (number - min_)//min_gap
			curr: Bucket = buckets[index]
			curr.min_number = (min(curr.min_number, number) 
							   if curr.min_number is not None else number)
			curr.max_number = (max(curr.max_number, number)
							   if curr.max_number is not None else number)
		
		return buckets
