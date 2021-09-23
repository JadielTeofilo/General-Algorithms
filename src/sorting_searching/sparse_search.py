"""
Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.

In - words: List[str], target: str
Out - index: int

['abc', '', '', '', '', '', '', 'ac', '', 'ba', '', '', 'bb']

What happens if the input has duplicates?
Return any index


O(logn) time complexity n being size of list on the best case
O(n) time complexity on worst case

What happens when empty string is the target
The way we did it will return None

"""
from typing import List, Optional


def sparse_search(words: List[str], target: str) -> Optional[int]:
	""" 
		Finds index of target on words, words being a 
		ordered list of strings with some empty string 
		in between.
		
		Returns:
		index of target or None if not present
	"""
	
	return binary_search(words, target, 
						 start=0, end=len(words) - 1)


def binary_search(words: List[str], target: str, 
 				  start: int, end: int) -> Optional[int]:
	""" Modified binary search that handles empty 
		values among the input """
	if start > end: 
		return
	mid: int = (start + end) // 2
	# Tries both sides if current is an empty string
	if words[mid] == '':
		mid = find_closest_valid_mid(words, mid, start, end)
	if words[mid] == target:
		return mid
	if mid is None:
		return
	if words[mid] > target:
		return binary_search(words, target, start, mid - 1)
	return binary_search(words, target, mid + 1, end)


def find_closest_valid_mid(words: List[str], current_mid: int, 
						  start: int, end: int) -> int:
	""" Finds the closest index that has non empty string in it """
	left: int = current_mid
	right: int = current_mid
	while True:
		left -= 1
		right += 1
		if left >= start and words[left] != '':
			return left
		if right <= end and words[right] != '':
			return right
		if right > end and left < start:
			break
	return


print(sparse_search(['abc', '', '', '', '', '', '', 'ac', '', 'ba', '', '', 'bb'], 'bb'))
print(sparse_search(['abc', '', '', '', '', '', '', 'ac', '', 'ba', '', '', 'bb'], 'abc'))
print(sparse_search(['abc', '', '', '', '', '', '', 'ac', '', 'ba', '', '', 'bb'], 'ac'))
print(sparse_search(['abc', '', '', '', '', '', '', 'ac', '', 'ba', '', '', 'bb'], 'tac'))
import pdb;pdb.set_trace()	
