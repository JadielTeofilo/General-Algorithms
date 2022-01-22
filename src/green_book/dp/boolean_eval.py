"""
Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
(AND), | (OR), and ^ (XOR), and a desi red boolean result value result, implement a function to
count the number of ways of parenthesizing the expression such that it evaluates to result. The
expression shou ld be fully parenthesized (e.g., (e) A (1» but not extraneously (e.g., ( ( (e» A (1)

In - expression: List[str], result: bool
Out - int

1^0|0|1






"""
from typing import List, Dict, Callable, Iterable
import collections


ExpressionResult = collections.namedtuple('ExpressionResult',
                                          'true false')


OPERATORS: List[str] = [
    '|', '^', '&'
]


def boolean_eval(exp: List[str], result: bool) -> int:
    """ Counts the ways that parenthesis can be 
        arranged on exp that lead to result """
    cache: Dict[str, int] = {}
    return eval_amount(exp, result, cache)


def eval_amount(exp: List[str], result: bool, 
                cache: Dict[str, int]) -> int:
    if len(exp) == 1:
        # Returns 1 if the expression matches the 
        # result, 0 other wise
        return int(bool(int(exp[0])) == result)
    
    exp_text: str = ''.join(exp)
    
    if cache.get(exp_text + str(result)):
        return cache[exp_text + str(result)]
    
    valid_amount: int = 0
    for index in find_operations(exp):
        left: ExpressionResult = ExpressionResult(
            eval_amount(exp[:index], True, cache),
            eval_amount(exp[:index], False, cache)
        )
        right: ExpressionResult = ExpressionResult(
            eval_amount(exp[index+1:], True, cache),
            eval_amount(exp[index+1:], False, cache)
        )
        valid_amount += get_amount_by_opeartor[exp[index]](
            left, right, result
        )
    
    cache[exp_text + str(result)] = valid_amount
    return valid_amount


def find_operations(exp: List[str]) -> Iterable[int]:
    """ Finds the indexes of all expression operators """
    for index, item in enumerate(exp):
        if item in OPERATORS:
            yield index 


def or_amount_finder(right: ExpressionResult, 
                     left: ExpressionResult, result: bool) -> int:
    """ Finds number of ops that match result """
    if result:
        return left.true * right.true + left.false * right.true + left.true * right.false
    return left.false * right.false


def and_amount_finder(right: ExpressionResult, 
                      left: ExpressionResult, result: bool) -> int:
    """ Finds number of ops that match result """
    if result:
        return left.true * right.true
    return left.false * right.false + left.false * right.true + left.true * right.false


def xor_amount_finder(right: ExpressionResult, 
                      left: ExpressionResult, result: bool) -> int:
    """ Finds number of ops that match result """
    if result:
        return left.false * right.true + left.true * right.false
    return left.false * right.false + left.true * right.true


get_amount_by_opeartor: Dict[str, Callable] = {
        '|': or_amount_finder,
        '&': and_amount_finder,
        '^': xor_amount_finder,
}

print(boolean_eval(list('1^0|0|1'), False))
print(boolean_eval(list('0&0&0&1^1|0'), True))
import pdb;pdb.set_trace()
