"""
Permutations without Dups: Write a method to compute all permutations of a string of unique
characters.



O(n^2*n!) time complexity where n is the size of the string



"""
from typing import Iterable, List


def permutations(word: str) -> Iterable[str]:
    chars_on_word: List[str] = [char for char in word]
    yield from permutation_helper(chars_on_word, 
                                  current_permutation=[])
    

def permutation_helper(chars: List[str], 
                       current_permutation: List[str]) -> Iterable[str]:
    if not chars:
        yield ''.join(current_permutation)
    
    for index, char in enumerate(chars):
        other_chars: List[str] = chars[:index] + chars[index + 1:]
        yield from permutation_helper(other_chars, 
                                      current_permutation + [char])
        

print([a for a in permutations('jadie')])
    
