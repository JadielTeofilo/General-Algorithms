"""
There are certain problems which are asked in the interview to also check how you take care of overflows in your problem.

This is one of those problems.

Please take extra care to make sure that you are type-casting your ints to long properly and at all places. Try to verify if your solution works if number of elements is as large as 105

    Food for thought :

        Even though it might not be required in this problem, in some cases, you might be required to order the operations cleverly so that the numbers do not overflow.
        For example, if you need to calculate n! / k! where n! is factorial(n), one approach is to calculate factorial(n), factorial(k) and then divide them.
        Another approach is to only multiple numbers from k + 1 ... n to calculate the result.
        Obviously approach 1 is more susceptible to overflows.

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:
3 1 2 5 3

real_sum = 14 
sums = 15 1 2 3 4 5
J = -1

1 4 9 16 25 = squares = 55
9 1 4 25 9 = real_squares = 48
K = -7




Output:[3, 4] 

A = 3, B = 4

expected_sum = n*(n-1)//2
sum - expected_sum = A - B
J = real_sum - sums = A - B
J = A - B
A = J + B

expected_product
sum - expected_product = A^2 - B^2
K = real_squares - squares
K = (J+B)^2 - B^2
K = J^2 + 2JB + B^2 - B^2
K = J^2 + 2*JB
(K - J^2)//(2*J) = B

A = J + B

1 2 3 4
1 4 9 16


In - numbers: List[int]
Out - List[int]

"""
from typing import List, Iterable


class Solution:
	# @param A : tuple of integers
	# @return a list of integers
	def repeatedNumber(self, numbers: List[int]) -> List[int]:
		n: int = len(numbers)
		sums: int = (n*(n+1))//2
		squares: int = self.find_squares(range(n+1))
		real_sums: int = sum(numbers)
		real_squares: int = self.find_squares(numbers)
		K: int = real_squares - squares
		J: int = real_sums - sums
		missing: int = (K - int(J**2))//(2*J)
		duplicated: int = J + missing
		return [duplicated, missing]
	
	def find_squares(self, numbers: Iterable[int]) -> int:
		squares: int = 0
		for number in numbers:
			squares += int(number**2)
		return squares



