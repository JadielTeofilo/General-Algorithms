"""
Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
(AND), | (OR), and ^ (XOR), and a desi red boolean result value result, implement a function to
count the number of ways of parenthesizing the expression such that it evaluates to result. The
expression shou ld be fully parenthesized (e.g., (e) A (1» but not extraneously (e.g., ( ( (e» A (1)

In - expression: List[str], result: bool
Out - int

1 & 0 | O ^ 1 = 1

1
0
1


^
&

O(n^2*n!) time complexity where n is the amount of operators
O(n) space where n is the amount of operators


'1^0|0|1'

(1^0)|(0|1)

"""
from typing import List, Dict, Callable, Tuple


OPERATIONS: Dict[str, Callable] = {
    '&': lambda x, y: x & y,
    '|': lambda x, y: x | y,
    '^': lambda x, y: x ^ y,
}


def boolean_eval(exp: List[str], result: bool) -> int:
    """
        Finds the amount of valid expressions 
        considering different parenthesis placing
    """
    operators: List[str] = find_operators(exp)
    values: List[bool] = find_values(exp)
    # Counter to store the amount of valid expressions
    valid_expressions: Dict[str, int] = {'sum': 0}
    boolean_eval_helper(values, operators, result, valid_expressions)
    return valid_expressions['sum']


def find_operators(exp: List[str]) -> List[str]:
    ops: List[str] = ['&', '|', '^']
    return [item for item in exp if item in ops]


def find_values(exp: List[str]) -> List[bool]:
    return [bool(item) for item in exp if item.isdigit()]


def boolean_eval_helper(values: List[bool], operators: List[str],
                        result: bool, 
                        valid_expressions: Dict[str, int]) -> None:
    if not operators:
        # Adds one to the valid expressions if the result is right
        valid_expressions['sum'] += int(values[0] == result)
        return
    for index in range(len(operators)):
        new_operators, new_values = apply_op(
            index, operators, values
        )
        boolean_eval_helper(new_values, new_operators, result, valid_expressions)


def apply_op(index: int, operators: List[str], 
             values: List[bool]) -> Tuple[List[str], List[bool]]:
    """ Applies operator on the given index """
    left: bool = values[index]
    right: bool = values[index + 1]
    result: bool = OPERATIONS[operators[index]](left, right)
    new_values: List[bool] = values[:index] + [result] + values[index + 2:]
    new_operators: List[str] = operators[:index] + operators[index + 1:]
    return new_operators, new_values
    


print(boolean_eval(list('1^0|0|1'), True))
print(boolean_eval(list('0&0&0&1^1|0'), True))
import pdb;pdb.set_trace()
    
    
