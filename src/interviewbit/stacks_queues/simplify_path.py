"""
Given a string A representing an absolute path for a file (Unix-style).

Return the string A after simplifying the absolute path.

Note:

    Absolute path always begin with ’/’ ( root directory ).

    Path will not have whitespace characters.


Input 1:
    A = "/home/"
Output 1:
    "/home"

Input 2:
    A = "/a/./b/../../c/"
Output 2:
    "/c"


we slipt on the / 
iterate on the folders
if ., do nothing
if .. pop from the stack

with the stack, join / and add it to the beginning


"""
from typing import List


class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, path):
        """
        a . b .. .. c 
        """
        folders: List[str] = path.split('/')
        stack: List[str] = []
        for folder in folders:
            if folder in {'.', ''}:
                continue
            if folder == '..':
                if stack:
                    stack.pop()
                continue
            stack.append(folder)
        result: str = '/' + '/'.join(stack)
        return result
