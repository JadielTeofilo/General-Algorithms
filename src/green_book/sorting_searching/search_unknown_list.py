"""
Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
method. It does, however, have an e lementAt (i) method that returns the element at index i in
0(1) time. If i is beyond the bounds of the data structure, it returns - 1. (For this reason, the data structure only supports positive integers.) Given a Listy which contains sorted, positive integers, find the index at which an element x occurs. If x occurs multiple times, you may return any index. 


In - numbers: List[int] (that can not be used len() upon), target: int
Out - index:int

find the bounderies for a binary search
[2 4 5 6 7 9 10 29 39]
last=4
curr=8
t = 9


O(log(n)) time complexity where n is the size of the list
O(log(n)) space for the recursion

"""
from typing import List
import collections


Limits = collections.namedtuple('Limits', 'start end')


def sorted_search_no_size(numbers: List[int], target: int) -> int:
	""" Finds element on list without using len() function """
	limits: Limits = find_limits(numbers, target)
	return binary_search(numbers, target, limits.start, limits.end)


def find_limits(numbers: List[int], target: int) -> Limits:
	""" Finds boundery for where the target is in O(log(n)) """
	last: int = 0
	current: int = 1
	# Doubles until passes the target element
	while (element_at(numbers, current) != -1
		   and numbers[current] < target):
		last = current
		current *= 2
	return Limits(last, current)
		

def element_at(numbers: List[int], index: int) -> int:
	try:
		return numbers[index]
	except IndexError:
		return -1


def binary_search(numbers: List[int], target: int, 
				  start: int, end: int) -> int:
	if start > end:
		return -1
	mid: int = (start + end) // 2
	if element_at(numbers, mid) == -1:
		return binary_search(numbers, target, 
							 start, mid - 1)
	if numbers[mid] == target:
		return mid
	if numbers[mid] > target:
		return binary_search(numbers, target, 
							 start, mid - 1)
	return binary_search(numbers, target, mid + 1, end)


print(sorted_search_no_size([1,3,4,6,7,9,13,25,76,355,766,1999], 766))
print(sorted_search_no_size([1,3,4,6,7,9,13,25,76,355,766,1999], 5))
print(sorted_search_no_size([1,3,4,6,7,9,13,14,23,25,76,355,766,1999], 25))
