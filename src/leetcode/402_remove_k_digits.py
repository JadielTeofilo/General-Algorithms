"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

3
1 5 6 4 3
=
1 3

1 5 1 1 1
=
11

1
1 4 1 1 5
= 1 1 1 5

In - number: str, remove: int
Out - int

What you want is to remove on element if there is at least one element smaller then it k elements to the right.
That is where the Monotonic stack cames in, cuz it allows to map bigger elements with smaller elements from left to right

1 5 6 3

1 5 3

Insert on the stack if empty or if the peak is smaller 
if bigger, pop from the stack until peak is smaller/equal
    only pop max of remove times, when reached, add remaining elements to stack and stop iteration 

check remove, if something left, remove from the end

turn list into str then into int


O(n) space and time where n is the size of number



"""
from typing import List


class Solution:
    def removeKdigits(self, number: str, remove: int) -> str:
        stack: List[str] = []
        for i, char in enumerate(number):
            if not stack or stack[-1] < char:
                stack.append(char)
                continue
            # Removes if peak of stack is bigger 
            while stack and stack[-1] > char and remove > 0:
                remove -= 1 
                stack.pop()
            if remove == 0:
                stack.extend(list(number[i:]))
                break
            stack.append(char)
        # Removes the remaining elements from the end
        while remove > 0:
            remove -= 1
            stack.pop()

        return ''.join(stack) or '0'


