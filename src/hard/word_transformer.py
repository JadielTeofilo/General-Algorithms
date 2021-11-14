"""
Word Transformer: Given two words of equal length that are in a dictionary, write a method to
transform one word into another word by changing only one letter at a time. The new word you get
in each step must be in the dictionary.

Is this problem going to be run more than once?
Interviewr: What would change then? I could build a graph and store the relations, after that, the problem becames a find a path problem

Is this word made of only english letters?
yes

What if there is more than one way?
just return one

In - origin: str, target: str, dictionary: Set[str]
Out - List[str]


Iterate on the dictionary finding all words that are one letter away, recurse on the all possibilities, keeping a visited

Use memoization to keep track of wheather a word can get to the target

O(d^2*o) where d is the amount of words in the distionary and o is the size of the original string
O(d^2) space complexity


"""
from typing import List, Set, Dict


Cache = Dict[str, List[str]]


def word_transformer(origin: str, target: str, 
                     dictionary: List[str]) -> List[str]:
    # TODO validate the input
    cache: Cache = {}
    visited: Set[str] = set()
    return transformer_helper(origin, target, 
                              dictionary, cache, visited)

def transformer_helper(origin: str, target: str, 
                       dictionary: List[str],
                       cache: Cache, visited: Set[str]) -> List[str]:
    visited.add(origin)
    if origin == target:
        return [target]
    if origin in cache:
        return cache[origin]
    for word in dictionary:
        if not is_one_away(origin, word) or word in visited:
            continue
        path: List[str] = transformer_helper(
            word, target, dictionary, cache, visited
        )
        if path:
            cache[origin] = [origin] + path
            return cache[origin]
    cache[origin] = []
    return cache[origin]
    

def is_one_away(left: str, right: str) -> bool:
    """
        Checks for a one character difference, 
        on same size strings
    """
    if len(left) != len(right):
        return False
    diff: int = 0 
    for i in range(len(left)):
        if left[i] != right[i]:
            diff += 1
    return diff == 1  # True if exactly one diff away


print(
    word_transformer(
        'damp', 'like', ['damp', 'lamp', 'dump', 'dimp', 'divp', 'dive', 'lime', 'dime', 'like', 'limp']
    )
)
