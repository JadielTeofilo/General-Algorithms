"""
You are given a binary string A(i.e. with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.



1011101

1010001


global max_sum
local max_sum
size keeps adding while localsum >=0, goes to 0 otherwise
max_interval - set when we see zeros
loops on digits
	case zero it adds 1 else -1
	it uses the local max if it is >= 0
	keep track of the size 

keep track of max contingous zeros
keep track of starting position
go greedy on the array

O(n) where n is the size of digits

In - digits: str
Out - pair: Pair



"""
from typing import List, Optional, Tuple


def flip(digits: str) -> List[int]:
	global_max_sum: int = 0
	local_max_sum: int = 0
	size: int = 0
	end_index: Optional[int] = None
	for index, digit in enumerate(digits):
		current: int = 1 if digit == '0' else -1
		if local_max_sum >= 0:
			local_max_sum += current
		else:
			local_max_sum = current
		if local_max_sum > global_max_sum:		
			global_max_sum = local_max_sum
			end_index = index
	if end_index is None:
		return []
	return [
		find_start_index(digits, end_index) + 1, 
		end_index + 1
	]

def find_start_index(digits: str, end_index: int) -> int:
	last_negative: Optional[int] = None
	curr_max: int = 0
	for index, digit in enumerate(digits[:end_index]):
		curr_value = 1 if digit[index] == '0' else -1
		if curr_max >= 0:
			curr_max += curr_value
		else:
			curr_max = curr_value
		if curr_max < 0:
			last_negative = index
	if last_negative is None:
		return 0
	return last_negative + 1


			
