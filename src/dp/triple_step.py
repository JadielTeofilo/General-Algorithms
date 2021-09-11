"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.


In - number: int 

Out - int



					5
				4
			3
		2
	1
0

f(n) = f(n - 1) + f(n - 2) + f(n - 3)

O(n) time complexity
O(1) space complexity


"""
from typing import List


def triple_step(number: int) -> int:
	"""
		Finds number of possible ways kid can go up stairs
		being able to jump, 1, 2 or 3 steps at a time
	"""
	cache: List[int] = [0, 1, 2, 3]  # Dp cache

	if number < 4:
		return cache[number]

	for i in range(3, number):
		aux: int = sum(cache)  # Recurence function
		cache[1] = cache[2]
		cache[2] = cache[3]
		cache[3] = aux

	return cache[-1]



import pdb;pdb.set_trace()
	
