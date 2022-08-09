"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.

Note:

    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


In 

    word: str  # word[i] in ['0-9', ' ', '[+-]', '.'] & 0 <= len(word) <= 200

Out
    number: int


check for empty string
find the index of the first non white space char
check for sign, set sign variable, add one to index if the sign exists
iterate on index while we have digits
    check if we would overflow, in this case return the limit num
        we check if number > INT_MAX // 10, it means that number * 10 will be bigger then INT_MAX
        if number == INT_MAX // 10, for the INT MAX we know that you can add up to 7 (cuz it is 2147483647 and the // 10 = 214748364)


O(N) time complexity where N is the size of word
O(1) space complexity
"""


MIN_INT = - 2 ** 31
MAX_INT = 2 ** 31 - 1


class Solution:
    def myAtoi(self, word: str) -> int:
        index: int = 0
        if not word: 
            return 0
        for index in range(len(word)):
            if word[index] != ' ':
                break
        else:
            return 0
        sign: int = 1
        if word[index] in ['-', '+']:
            sign = -1 if word[index] == '-' else 1
            index += 1
        result: int = 0
        for index in range(index, len(word)):
            if not word[index].isdigit():
                return sign * result
            if would_overflow(result, ord(word[index]) - ord('0'), sign):  # TODO
                return MIN_INT if sign < 0 else MAX_INT
            result = result * 10 + ord(word[index]) - ord('0')
        return sign * result

def would_overflow(number: int, addition: int, sign: int) -> int:
    """
    we want to check 
        (MIN_INT + addition) / 10 > number
    """
    return number > MAX_INT / 10 or number == MAX_INT / 10 and addition > 7

