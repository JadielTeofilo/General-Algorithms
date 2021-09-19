"""

Followup: What if it was not unique chars

Permutations with Duplicates: Write a method to compute all permutations of a string whose characters are not necessarily unique. The list of permutations should not have duplicates.

"""
from typing import List, Iterable, Set


def permutations(word: str) -> Iterable[str]:
    chars: List[str] = [char for char in word]
    yield from permutations_helper(chars, current_permutation=[])
   
   
def permutations_helper(chars: List[str], 
                        current_permutation: List[str]) -> Iterable[str]:
    
    if not chars:
        yield ''.join(current_permutation)
    
    visited: Set[str] = set()
    
    for index, char in enumerate(chars):
        if char in visited:
            continue
        visited.add(char)
        other_chars: List[str] = chars[:index] + chars[index + 1:]
        yield from permutations_helper(other_chars, 
                                       current_permutation + [char])
        


print([a for a in permutations('jedie')])
print(len([a for a in permutations('jedie')]))
