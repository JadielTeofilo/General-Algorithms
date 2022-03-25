"""
How many minimum numbers from fibonacci series are required such that sum of numbers should be equal to a given Number N?

Note : repetition of number is allowed.

Example:

N = 4
Fibonacci numbers : 1 1 2 3 5 .... so on
here 2 + 2 = 4 
so minimum numbers will be 2 





Generate all numbers up to limit (O(n))

we now have a list of nums that we want to find the min nums that get to the value

get the biggest number smaller equal to the target
call the recursion with target - number and end=index_of_biggest

solve(target, fibonacci, end)


Pattern last splitting resource, notice that you need to take the biggest possible number that does not surpress the target. But remember at the end you might want to use the 1 twice to make the two. This greedy approach does not work with all cases.


O(log(n)) time where n is the size of the input cuz there are log(n) fibo nums smaller then n
O(log(n)) space from the stack

In - target: int
Out - int

"""
from typing import List


class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, target: int) -> int:
        if target == 0:
            return 0
        nums: List[int] = self.get_fib_smaller(target)
        return self.find_optimal_sum(target, nums, len(nums) - 1)

    def find_optimal_sum(self, target: int, nums: List[int], 
                         end: int) -> int:
        if target < 2:
            return target
        curr: int = nums[end]
        return 1 + self.find_optimal_sum(target - curr, nums, end - 1)

    def get_fib_smaller(self, target: int) -> List[int]:
        nums: List[int] = [1, 1]
        last: int = 1
        i: int = 2
        while last < target:
            nums.append(nums[i - 1] + nums[i - 2])
            last = nums[i]
            i += 1
        if nums[-1] > target:
            nums.pop()
        return nums
