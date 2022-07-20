""""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


s consists of digits, '+', '-', '(', ')', and ' '.

Care about unary operation (-1)

-1 + 2

we can think of the minus as always applied to the element on the right, and always do additions


stacks are usually the way to go

nums: List[int] = [
-1


]



ops: List[str] = [

]

when we intert a number we check if there is already an operator, if there is we apply it (if no other number we just apply on the number (op1 * num))

- (1 + 1) - ((3 + 2) - 1)


nums: List[int] = [
-2 | 4

]



ops: List[str] = [
- 
]

maybe use recursion when we find an opening parenthesis
    use a start Dict[str, int] {'value': 0} to keep track of where the iteration is
when we see the closing parenthesis we return the value on the stack


O(n) time complexity
O(n) space complexity
"""
import dataclasses
from typing import List, Dict, Callable


OPS: Dict[str, Callable] = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
}
 

@dataclasses.dataclass
class Pointer:
    start: int = 0


class Solution:
    def calculate(self, equation: str) -> int:
        return solve(equation, Pointer())


def solve(equation: str, start: Pointer) -> int:
    if start.start >= len(equation):
        return 0
    ops: List[str] = []
    nums: List[int] = []
    while start.start < len(equation):
        curr: str = equation[start.start]
        start.start += 1
        if curr == ' ':
            continue
        if curr in OPS:
            ops.append(curr)
        elif curr == ')':
            return nums[0]
        elif curr == '(':
            apply_number(solve(equation, start), ops, nums)
        else:
            number: int = int(curr)
            while (start.start < len(equation) and 
                   equation[start.start].isdigit()):
                number *= 10
                number += int(equation[start.start])
                start.start += 1
            apply_number(number, ops, nums)
    return nums[0]


def apply_number(number: int, ops: List[str], nums: List[int]) -> None:
    if not ops:
        nums.append(number)
        return
    left: int = nums.pop() if nums else 0
    nums.append(OPS[ops.pop()](left, number))

