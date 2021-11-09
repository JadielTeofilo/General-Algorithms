"""
Missing Two: You are given an array with all the numbers from 1 to N appearing exactly once,
except for one number that is missing. How can you find the missing number in 0 (N) time and
O( 1) space? What if there were two numbers missing

In - numbers: List[int]
Out - int


sum = (n(n - 1))/2
O(n) time complexity
O(1) space complexity 



"""
import math
from typing import List, Tuple, Iterable
import unittest


def missing_one_number(numbers: List[int]) -> int:
    if not numbers:
        raise ValueError('Empty input')
    n: int = len(numbers) + 1
    return int((n * (n + 1)) / 2) - sum(numbers)


def missing_two_numbers(numbers: List[int]) -> Tuple[int, int]:
    sum_of_missing: int = get_sum_of_missing(numbers)  #TODO
    product_of_missing: int = get_product_of_missing(numbers)  #TODO
    y: int = int(math.sqrt(product_of_missing/sum_of_missing))
    x: int = sum_of_missing - y
    return x, y


def get_sum_of_missing(numbers: List[int]) -> int:
    n: int = len(numbers) + 2
    return int((n*(n+1))/2) - sum(numbers)


def get_product_of_missing(numbers: List[int]) -> int:
    return product(range(1, len(numbers) + 3)) - product(numbers)


def product(numbers: Iterable[int]) -> int:
    product_value: int = 1
    for number in numbers:
        product_value *= number
    return product_value
    

class Test(unittest.TestCase):

    def test(self) -> None:
        self.assertEqual(missing_one_number([1,2,3,4,5,6,7,9,10]), 8)
        self.assertEqual(missing_two_numbers([1,3,4,5,6,7,9,10]), (2,8))


if __name__ == '__main__':
    unittest.main()
