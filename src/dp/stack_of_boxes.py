"""
 Stack of Boxes: You have a stack of n boxes, with widths w heights h and depths d The boxes
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
larger than the box above it in width, height. and depth. Implement a method to compute the
height of the tallest possible stack. The height of a stack is the sum of the heights of each box


In - boxes: List[Box]

Out - int

Is the height always an integer?
Yes

Brute force
consider each box as the first and recurse finding the next possible box
Optimization:
Cache the result for a given box

Sorting wont metter cuz one box by it self might have the highest height.

O(n^2) time complexity, n being the number of boxes, the memoization will make us recurse on it n times, on each iteration we will go through at most n boxes

O(n^2) space, n being the number of boxes, from recursion

"""
from typing import List, Dict, Optional
import collections
import math


Box = collections.namedtuple('Box', 'width height depth')
Cache = Dict[Optional[Box], int]


def max_boxes_stack_height(boxes: List[Box]) -> int:

	cache: Cache = {}
	boxes.sort()
	boxes.reverse()
	return max_height_helper(
		curr_height=0, boxes=boxes, index=0,
		curr_box=None, cache=cache
	)


def max_height_helper(curr_height: int, boxes: List[Box],
					  index: int, curr_box: Optional[Box],
					  cache: Cache) -> int:
	if index >= len(boxes):
		return curr_height
	if cache.get(curr_box):
		return cache[curr_box]
	max_height: int = curr_height
	# Tests every box starting from index
	for i in range(index, len(boxes)):
		box = boxes[i]
		if not is_valid(box, curr_box):
			continue
		new_height: int = max_height_helper(
			curr_height + box.height, boxes,
			index + 1, box, cache
		)
		max_height = max(max_height, new_height)
	cache[curr_box] = max_height
	return cache[curr_box]
		


def is_valid(box: Box, constraint_box: Box) -> bool:
	""" Validates box being smaller then the constraint box """
	if not constraint_box:
		return True
	return (box.width < constraint_box.width and
 	    	box.height < constraint_box.height and
	 	    box.depth < constraint_box.depth)
	

print(max_boxes_stack_height([Box(1,2,1), Box(2,4,5)]))
import pdb;pdb.set_trace()	
