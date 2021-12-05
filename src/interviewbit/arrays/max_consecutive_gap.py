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
from typing import List, Set


@dataclasses.dataclass
class Bucket:
    max_number: Optional[int]
    min_number: Optional[int]
    start: int 
    end: int


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, numbers: List[int]) -> int:
        if len(numbers) < 2:
            return 0
        buckets: List[Buckets] = self.build_buckets(numbers)  # TODO
        self.fill_buckets(buckets, numbers)  #TODO
        max_gap: int = 0
        last: Bucket = buckets[0]
        for bucket in buckets[1:]:
            max_gap = max(max_gap, bucket.min_number - last.max_number)
            last = bucket
        return max_gap
          
    def build_buckets(self, numbers: List[int]) -> List[Bucket]:
        max_: max(numbers) 
        min_: min(numbers)
        min_gap: int = (max_ - min_) // len(number) - 1 
        buckets: List[Bucket] = []
        for number in range(min_, max_+1, min_gap):
            # Non inclusive at end
            buckets.append(Bucket(None, None, number, number + min_gap))
        return buckets

    def fill_buckets(buckets: List[Bucket], numbers: List[int]) -> None:
       


