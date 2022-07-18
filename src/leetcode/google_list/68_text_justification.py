"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.



current_line: List[str]
current_space: int 
result: List[str]

[this is a movie and such]
12
this, is, a

iterate on the words keeping track of the current line
when we get to a word that does not fit, we will clean the current line and initialize a new line
check current_space < len(word) + 1 (1 from the space), then do the above

If empty just insert it and decrease the current_space

take the current_space//(len(current_line) - 1)  Be aware of 0 division, current_space % (len(current_line) - 1) we add on the left most intersection
every word should already have a space with it


at the last iteration generate the line


O(n*w) time complexity where n is num of words and w the size
O(m) space where m is the max width
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr_line: List[str] = []
        current_space: int = maxWidth
        result: List[str] = []
        for word in words:
            if curr_line and current_space < len(word) + 1:
                clean_line(curr_line, result, current_space)
                current_space = maxWidth
                curr_line = []
            if not curr_line:
                curr_line.append(word)
                current_space -= len(word)
                continue
            curr_line.append(' ' + word)
            current_space -= (len(word) + 1)
        if curr_line:
            clean_line(curr_line, result, current_space, is_last=True)
        return result

def clean_line(line: List[str], result: List[str], space: int, is_last=False) -> None:
    if len(line) == 1:
        result.append(line[0] + ' ' * space)
        return
    if is_last:
        result.append(''.join(line) + ' ' * space)
        return
    divided_space: int = space // (len(line) - 1)
    left_space: int = space % (len(line) - 1)
    first_part: str = (' ' * (divided_space + 1)).join(line[:left_space]) + (' ' * (divided_space + 1) if left_space > 0 else '')
    second_part: str = (' ' * divided_space).join(line[left_space:])
    result.append(first_part + second_part)

