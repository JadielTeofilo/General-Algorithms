"""
You are given an integer array nums of length n and an integer numSlots such that 2 * numSlots >= n. There are numSlots slots numbered from 1 to numSlots.

You have to place all n integers into the slots such that each slot contains at most two numbers. The AND sum of a given placement is the sum of the bitwise AND of every number with its respective slot number.

    For example, the AND sum of placing the numbers [1, 3] into slot 1 and [4, 6] into slot 2 is equal to (1 AND 1) + (3 AND 1) + (4 AND 2) + (6 AND 2) = 1 + 1 + 0 + 2 = 4.

Return the maximum possible AND sum of nums given numSlots slots.


In - nums: List[int], slots: int 
Out - int


nums = [2, 6, 3, 1]
slots = 3

00 00 00

Try to put each number on each slot

					2 6 3 1
		2_1 (6,3,1) 	2_2 (6,3,1) 			2_3 (6,3,1)

iterate on slots
	skip slots that are full
	call recursion using that slot
	

to use a slot update the mask setting the slot bit

depth recursion = N
branches = slots

bitmask of size slots*2
O(s*2^s*n) time complexity where s=slots n=size nums
O(2^s*n) space complexity


"""
from typing import Dict, Iterable, Tuple, List


Cache = Dict[Tuple[int, int], int]


class Solution:
	def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
		cache: Cache = {}
		return self.find_max_and_sum(nums, numSlots, 0, 0, cache)

	def find_max_and_sum(self, nums: List[int], slots: int, start: int,
						 mask: int, cache: Cache) -> int:
		if start >= len(nums):
			return 0
		if (start, mask) in cache:
			return cache[(start, mask)]
		max_sum: int = 0
		for slot in self.find_valid_slots(slots, mask):
			updated_mask: int = self.update_mask(mask, slot)
			max_sum = max(
				max_sum, 
				self.find_max_and_sum(nums, slots, start + 1, 
									  updated_mask, cache) + 
				(slot & nums[start])
			)
		cache[(start, mask)] = max_sum
		return cache[(start, mask)]

	def find_valid_slots(self, slots: int, mask: int) -> Iterable[int]:
		for slot in range(1, slots + 1):
			if self.is_valid(slot, mask):
				yield slot

	def is_valid(self, slot: int, mask: int) -> bool:
		return (not self.get_bit(mask, (slot - 1) * 2) or
				not self.get_bit(mask, (slot - 1) * 2 + 1))

	def update_mask(self, mask: int, slot: int) -> int:
		if not self.get_bit(mask, (slot - 1) * 2):
			return self.set_bit(mask, (slot - 1) * 2)
		return self.set_bit(mask, (slot - 1) * 2 + 1)
			
	def get_bit(self, number: int, index: int) -> int:
		return (number >> index) & 1

	def set_bit(self, number: int, index: int) -> int:
		return number | (1 << index)


if __name__ == '__main__':
	print(Solution().maximumANDSum([2,3], 2))
