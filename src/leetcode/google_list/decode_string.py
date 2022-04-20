"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].


2[a2[sse]]1[d]e

asssasssde

solve(encoded)

use a stack to get the inner elements

ssesse
essess

2
a
2



In - encoded: str
Out - str

"""
import dataclasses
from typing import List


@dataclasses.dataclass
class StackValue:
    k: int
    words: List[str]


class Solution:
    def decodeString(self, encoded: str) -> str:
        stack: List[StackValue] = []
        result: List[str] = []
        for char in encoded:
            if char.isdigit():
                if not stack or stack[-1].words:
                    stack.append(StackValue(0, []))
                curr: StackValue = stack[-1]
                curr.k = curr.k * 10 + int(char)
                curr.words.append(char)
                continue
            if char == '[':
                continue

            if char.isalpha():
                curr_word: str = char
            if char == ']':
                curr_word: str = self.get_word(stack[-1])
            if not stack:
                result.append(curr_word)
            else:   
                stack[-1].words.append(curr_word)
        return ''.join(result)
    
    def get_word(self, stack_value: StackValue) -> str:
        return ''.join(stack_value.words) * stack_value.k
        
