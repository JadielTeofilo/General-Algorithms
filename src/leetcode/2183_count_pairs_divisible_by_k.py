"""
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:

    0 <= i < j <= n - 1 and
    nums[i] * nums[j] is divisible by k.


a * b % k = 0


Think of factors 

A can be formed by diff pairs of factors:
if A = 16

1*16
2*8
4*4


A number with a factor i will form a pair with a number with a factor j if i * j is divisible by k.

It can be shown that if n1 * n2 % k == 0, then gcd(n1, k) * gcd(n2, k) % k == 0.

The gcd gives you a shared factor between the two numbers. so if you have a shared factor between a and k and between k and b, you can just iterate and search on those factors, there will be less factors then numbers, making it O(n*sqrt(k)) since there are at most sqrt factor pairs.

O(n*sqrt(k)) time
O(sqrt(k))

"""
import collections
from typing import List, Dict


class Solution:
	def countPairs(self, nums: List[int], k: int) -> int:
		gcds: Dict[int, int] = collections.defaultdict(int)
		result: int = 0
		for num in nums:
			curr_divisor: int = self.get_gcd(num, k)
			for divisor, count in gcds.items():
				if (divisor * curr_divisor) % k == 0:
					result += count
			gcds[curr_divisor] += 1
		return result

	def get_gcd(self, first: int, second: int) -> int:
		if second > first:
			return self.get_gcd(second, first)
		if second == 0:
			return first
		return self.get_gcd(second, first % second)
