"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].


qwe2[a2[sse]]1[d]e

qweasssasssde

Problem with number having more than one digit

The idea is to work like a program would with the calls being stacked


case [ (we put the old values on the stack and set new ones)
    we put curr_word in the stack
    we put curr_k in the stack

case alpha
    we add to curr_word
case digit
    we add to curr_k

case ]
    we get the last k pop()
    we get the curr_word 
    make curr_word be stack.pop() + curr_word * k

O(max K * n) time complexity where K if the digit multiplier n is the size of the string
O(m + n) space where m is num of digits in the input and n the num of letters


In - encoded: str
Out - str

"""
from typing import List, Union


class Solution:
    def decodeString(self, encoded: str) -> str:
        stack: List[Union[str, int]] = []
        curr_k: int = 0
        curr_word: str = ''
        for char in encoded:
            if char == '[':
                stack.append(curr_k)
                stack.append(curr_word)
                curr_k = 0
                curr_word = ''
            elif char.isdigit():
                curr_k = curr_k * 10 + int(char)
            elif char.isalpha():
                curr_word = curr_word + char
            elif char == ']':
                last_word: Union[str, int] = stack.pop()
                last_k: Union[str, int] = stack.pop()
                curr_word = last_word + (curr_word * last_k)
        return curr_word
