"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example :

Given numerator = 1, denominator = 2, return "0.5"
Given numerator = 2, denominator = 1, return "2"
Given numerator = 2, denominator = 3, return "0.(6)"

In: dividend: int, divisor: int
Out: str

1/2
Take the integer part off:
    integet = dividend//divisor
work on the rest

keep a smaller_streak: int = 1
no need to keep a has_dot but just know that it starts as True
keep a dict from dividend to index on the quotient

loop while dividend is diff than zero and has not occurred before
    if dividend is bigger, just divide and receive the mod
    update smaller_streak and 

outside the loop, if it occurred before, 


"""
from typing import List, Dict

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, dividend: int, divisor: int) -> str:
        integer: str = str(dividend // divisor)
        fraction: str = self.find_fraction(abs(dividend % divisor), abs(divisor))
        return integer + fraction

    def find_fraction(self, dividend: int, divisor: int) -> str:
        if dividend == 0:
            return ''
        quotient: List[int] = []
        dividend *= 10  # Already does the first multiplication
        smaller_streak: int = 1
        visited: Dict[int, int] = {}
        while dividend != 0 and dividend not in visited:
            if dividend > divisor:
                visited[dividend % divisor] = len(quotient)
                quotient.append(dividend // divisor)
                dividend = dividend % divisor
                smaller_streak = 0
            else:
                if smaller_streak > 0:
                    quotient.append(0)
                dividend *= 10
                smaller_streak += 1
        result: List[str] = [str(number) for number in quotient]
        if dividend != 0:
            self.add_parenthesis(result, visited[dividend])
        return '.' + ''.join(result)

    def add_parenthesis(self, result: List[str], start: int) -> None:
        result[-1] = result[-1] + ')'
        result[start] = '(' + result[start]


