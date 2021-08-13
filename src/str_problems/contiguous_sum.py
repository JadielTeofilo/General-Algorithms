import math
from typing import List, Union
import unittest


def contiguous_sum(nums: List[int]) -> int:
    max_sum: Union[int, float] = -math.inf
    local_sum: int = 0
    for num in nums:
        local_sum = max(local_sum + num, num)
        max_sum = max(max_sum, local_sum)
    return int(max_sum)


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(contiguous_sum([2, -8, 3, -2, 4, -10]), 5)


if __name__ == '__main__':
    unittest.main()
