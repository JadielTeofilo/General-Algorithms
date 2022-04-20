"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.


Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

solve(index, )



3
*


we insert on the stack. The stopping point is when we find a operator we then pop two numbers from stack and apply the operation.


O(n) time and space where n is the num of elements on the input

In - tokens: List[str]
Out - int


"""
from typing import List, Callable, Dict


OPS = {'/', '*', '-', '+'}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[str] = []
        for token in tokens:
            if token in OPS:
                right: str = stack.pop()
                left: str = stack.pop()    
                token = self.make_op(token, left, right)
            stack.append(int(token))
        return stack[0]

    def make_op(self, op: str, number: str, other: str) -> str:
        equivalency: Dict[str, Callable] = {
            '/': lambda x, y: int(x / y),
            '*': lambda x, y: x * y,
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
        }
        return equivalency[op](number, other)
