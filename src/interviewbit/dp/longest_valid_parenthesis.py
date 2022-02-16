"""
Given a string A containing just the characters ’(‘ and ’)’.

Find the length of the longest valid (well-formed) parentheses substring.

()(()
10010
01001


 ()(( ))
01012 10

  ) ) ) ( ( )
0-1-2-3-2-1-2

to validate we keep track of opennings and closings


build backtracking to go on every n^2 substrs


					()(())
		'(')								)
	'()'(		(	


()(())
322100
())((
10000
12100

))()((
111000    
110100

stack is an option
we want to find a valid substring 
)()(()



(

size 
0
0
2
2
2

the stack allows us to match opening and closing parentheses, with that you can get the size of the group of parentheses by subtracting the index. Now to group the groups, the following is necessary: insert a -1 index on the stack, and go from there (insert all indices of '('), always pop the curr and substract with what is left (which is the element to the left of the matching parenthesis (-1 if still the first)), if empty put the curr index.

keep a size counter 





we can go backwards filling dp
dp[-1] = 0
dp[i] = dp[i+1] + (1 if n[i] == '(' and closed > 0 else 0)


O(n) time complexity where n is the size of string
O(n) space complexity
"""
from typing import List


class Solution:
	# @param A : string
	# @return an integer
	def longestValidParentheses(self, parentheses: str) -> int:
		stack: List[int] = [-1]
		max_size: int = 0
		for i in range(len(parentheses)):
			if parentheses[i] == '(':
				stack.append(i)
			else:
				stack.pop()
				if not stack:
					stack.append(i)
				else:
					max_size = max(max_size, i - stack[-1])
		return max_size
		

