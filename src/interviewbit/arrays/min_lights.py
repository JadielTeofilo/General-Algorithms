"""
Problem Description

There is a corridor in a Jail which is N units long. Given an array A of size N. The ith index of this array is 0 if the light at ith position is faulty otherwise it is 1.

All the lights are of specific power B which if is placed at position X, it can light the corridor from [ X-B+1, X+B-1].

_ _ _ 1 _ _ _ _

Initially all lights are off.

Return the minimum number of lights to be turned ON to light the whole corridor or -1 if the whole corridor cannot be lighted.
Problem Constraints

1 <= N <= 1000

1 <= B <= 1000
Input Format

First argument is an integer array A where A[i] is either 0 or 1.

Second argument is an integer B.
Output Format

Return the minimum number of lights to be turned ON to light the whole corridor or -1 if the whole corridor cannot be lighted.

An option is to try all combinations, check them and then return 
Gready approach, at every step:
	iterate on the spots
		for every spot find the rightmost light that works
		continue from the next unlighten spot

O(n) time xomplexity where n is the size of the corridor
O(1) space complexity

Example Input
Input 1:
A = [ 0, 0, 1, 1, 1, 0, 0, 1].

	  	
B = 3

Input 2:
A = [ 0, 0, 0, 1, 0].
B = 3

Example Output
Output 1:
2

Output 2:
-1


Example Explanation

Explanation 1:

In the first configuration, Turn on the lights at 3rd and 8th index.
Light at 3rd index covers from [ 1, 5] and light at 8th index covers [ 6, 8].

Explanation 2:

In the second configuration, there is no light which can light the first corridor.
"""
from typing import List


class Solution:
	# @param A : list of integers
 	# @param B : integer
	# @return an integer
	def solve(self, lights: List[int], power: int) -> int:
		if power < 1:
			return -1
		i: int = 0 
		count: int = 0
		while i < len(lights):
			used_light: int = self.find_rightmost_light(lights, i, power)
			if used_light == -1:
				return -1
			count += 1
			i = used_light + power  # Goes to the next unlighten spot
		return count


	def find_rightmost_light(self, lights: List[int], 
							 i: int, power: int) -> int:
		start: int = max(0, i - power + 1)
		end: int = min(len(lights) - 1, i + power - 1)
		for i in range(end, start - 1, -1):
			if lights[i] == 1:
				return i
		return -1
			
		
