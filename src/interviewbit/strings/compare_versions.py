"""
Compare two version numbers version1 and version2.

        If version1 > version2 return 1,
        If version1 < version2 return -1,
        otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4


it might be good to add the second dot if there is only one
split on the dot
we can then just iterate on three spots, comparing
if they are equal, go to the next step if bigger or smaller, return
at the end return 0

In - left_version: str, right_version: str
Out - int


O(n+m)  time complexity where n and m are the sizes of the inputs
O(n+m) space

"""
from typing import List, Dict


Spots = List[str]


class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def compareVersion(self, left_version: str, 
					   right_version: str) -> int:
		dots: int = max(left_version.count('.'),
						right_version.count('.'))
		right_version = self.fill_when_needed(right_version, dots)
		left_version = self.fill_when_needed(left_version, dots)
		left_spots: Spots = self.get_spots(left_version)
		right_spots: Spots = self.get_spots(right_version)
		for left, right in zip(left_spots, right_spots):
			if int(left) > int(right):
				return 1
			elif int(left) < int(right):
				return -1
		return 0		

	def fill_when_needed(self, version: str, dots: int) -> str:
		filling: List[str] = []
		for _ in range(dots - version.count('.')):
			filling.append('.0')
		return version + ''.join(filling)

	def get_spots(self, version: str) -> List[str]:
		return version.split('.')

