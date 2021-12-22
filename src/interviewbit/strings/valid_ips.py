"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)


At each step three options 1, 2 or 3 digits
Three of depth Four 

Calculate the min nums we need at each step
this case is 11//4 = 2
If the first num is bigger then 2 or second/third bigger then 5 stop


							_
		25.							result=255. (remaininig = 25511135)
								255.25.					255.255.
													255.255.11.   255.255.111
									
								



O(1) considering that we ll ignore inputs bigger then 12
O(1) space same reason

In - ip: str
Out List[str]


"""
from typing import List


class Solution:
	# @param A : string
	# @return a list of strings
	def restoreIpAddresses(self, ip: str) -> List[str]:
		if len(ip) > 12 or len(ip) < 4:
			return []
		return self._solve(current='', remaining=ip, ip_class=0)

	def _solve(self, current: str, remaining: str, 
			   ip_class: int) -> List[str]:
		if not remaining and ip_class > 3:
			return [current]
		if not remaining or ip_class > 3:
			return []
		result: List[str] = []
		if current:
			current += '.'
		for size in range(1, min(4, len(remaining)+1)):
			if self._invalid(remaining[:size]):
				continue
			result.extend(
				self._solve(current+remaining[:size], 
							remaining[size:], ip_class+1)
			)
		return result
	
	def _invalid(self, remaining: str) -> bool:
		"""
			Valid strings are numbers from 1 to 255 
			and zero with single digits
		"""
		if len(remaining) > 1 and remaining[0] == '0':
			return True
		return not (1 <= int(remaining) <= 255)
