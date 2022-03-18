"""
You are given an array of integers nums. Perform the following steps:

    Find any two adjacent numbers in nums that are non-coprime.
    If no such numbers are found, stop the process.
    Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
    Repeat this process as long as you keep finding two adjacent non-coprime numbers.

Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.

The test cases are generated such that the values in the final array are less than or equal to 108.

Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.


The idea here is to use a stack, since the process has to be repeated as long as there are adjacent non comprime numbers, compare with top of stack, if non comprime, pop from the stack, generate the new number and keep comparing to the stack until done

O(nlog k) time where n is the num of elements and k is the biggest possible num
O(n) space where n is len of nums

"""

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        """
        Input: nums =
        [6,4,3,2,7,6,2]
                     -
        12 7 6
        Output: [12,7,6]

        result list
        add first to result

        iterate on numbers from second
        do gcd with top of result


        """
        if not nums:
            return []
        result = nums[:1]
        for i in range(1, len(nums)):
            # [287,41,49,287,899,23,23,20677,5,825]
            num = nums[i]
            while result and self.gcd(result[-1], num) > 1:
                top = result[-1]
                curr_gcd = self.gcd(top, num)
                result.pop()
                num = abs(top * num) // curr_gcd
            result.append(num)
        return result


    def gcd(self, a, b):
        if b > a:
            return self.gcd(b, a)
        if b == 0:
            return a
        return self.gcd(b, a % b)
