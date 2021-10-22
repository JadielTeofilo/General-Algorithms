"""
 Letters and Numbers: Given an array filled with letters and numbers, find the longest subarray with
an equal number of letters and numbers.

In - symbols: List[str]
Out - List[str]


1 1 a 1 1 a a 1 1 a
1 2 1 2 3 2 1 2 3 2
1 2 2 3 4 4 4 5 6 6
0 0 1 1 1 2 3 3 3 4
6 5 4 4 3 2 2 2 1 0
  _ _ _ _ _ _ _  


2 -1 2 -2 2 -1
   _    _    _

2  1 3  1 3  2


num_count: int 4
letter_count: int 2



"""
import collections
from typing import Dict, List, Any


Range = collections.namedtuple('Range', 'start end')


def letters_numbers(symbols: List[str]) -> List[str]:
	"""
		Finds the longest subarray with equal 
		letters and nums
	"""
	curr_count: int = 0
	cache: Any = collections.defaultdict(lambda: len(symbols))
	cache[0] = -1
	range_: Range = Range(-1, 0) 
	max_size: int = 0
	for index, symbol in enumerate(symbols):
		curr_count += 1 if symbol.isdigit() else -1
		if (cache.get(curr_count) is not None and
			index - cache[curr_count] > max_size):
			max_size = index - cache[curr_count]
			range_ = Range(cache[curr_count], index)
		cache[curr_count] = min(cache[curr_count], index)
	return symbols[range_.start+1:range_.end+1]


print(letters_numbers(list('11a11aa11a')))
import pdb;pdb.set_trace()




