"""

Calculator: Given an arithmetic equation consisting of positive integers,
 +, -, * and / (no parentheses). compute the result.
EXAMPLE
Input:
 2*3+5/6*3+15
Output:
 23.5

How is the input camming in, as a list or string
list
[2 * 3 + 5 / 6 * 3 + 15]

2 * 3 ### 5 / 6 * 3 ### 15


"""
from typing import List, Dict, Set, Callable


METHOD_TRANSLATION: Dict[str, Callable] = {
    '*': lambda left, right : left*right,
    '/': lambda left, right : left/right,
    '-': lambda left, right : left-right,
    '+': lambda left, right : left+right,
}


PRIORITY_OPERATIONS: Set[str] = {'*', '/'}


def equation_solver(equation: List[str]) -> float:
    """
    Equation solver, assumes valid equation without parenthesis
    """
    if not equation:
        raise ValueError('Empty input')
    stack: List[str] = []
    
    for element in equation:
        if element.isdigit():
            if should_add_to_the_stack(stack, element):
                stack.append(element)
            else:
                do_operation(stack, element)
        else:
            if not element in PRIORITY_OPERATIONS:
                do_remaining_operations(stack)  # Colapse the stack
            stack.append(element)

    do_remaining_operations(stack)
    return float(stack[0])


def should_add_to_the_stack(stack: List[str], element: str) -> bool:
    """
    Tells if element should be added to the stack or 
    should be applied the operation on 
    """
    if not stack:
        return True
    if stack[-1] in PRIORITY_OPERATIONS:
        return False
    return True


def do_operation(stack: List[str], element: str) -> None:
    """ Does opeartion with element and top operation of the stack """
    operator: str = stack.pop()
    left_digit: float = float(stack.pop())
    right_digit: float = float(element)
    stack.append(METHOD_TRANSLATION[operator](left_digit, right_digit))


def do_remaining_operations(stack: List[str]) -> None:
    """ Does all remaining operation on the stack, in place"""
    while len(stack) > 1:
        element: str = stack.pop()
        do_operation(stack, element)



print(equation_solver(['1', '+', '1']))
print(equation_solver(['2', '*', '3', '+', '5', '/', '6', '*', '3', '+', '15']))
    
    
    
    
