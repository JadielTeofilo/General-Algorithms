"""
Build all subarrays from list of integers without duplicates


O(n^2) time complexity where n is the size of the input
O(1) space
"""
from typing import List, Optional, Set, Iterator
import unittest


def build_subarrays(nums: List[int], start: int = 0, 
                    cache: Optional[Set[int]] = None) -> Iterator[List[int]]:
    if cache is None:
        cache = set()
    if start >= len(nums) or start in cache:
        return
    cache.add(start)
    for i in range(start, len(nums)):
        yield nums[start:i+1]
        yield from build_subarrays(nums, i + 1, cache)  


class Test(unittest.TestCase):

    def test_build_subarrays(self) -> None:
        nums: List[int] = [9,2,1,3,4,6,5,34]
        self.assertEquals(len(list(build_subarrays(nums))), (len(nums)*(len(nums)+1))//2 )


if __name__ == '__main__':
    unittest.main()
