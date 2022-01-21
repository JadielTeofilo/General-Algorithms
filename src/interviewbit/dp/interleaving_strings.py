"""
Given A, B, C, find whether C is formed by the interleaving of A and B.

Input Format:*

The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains a string, C.

Output Format:

Return an integer, 0 or 1:
    => 0 : False
    => 1 : True

In - left: str, right: str, target: str
Out - int  # 0 or 1

abc
cbf

cbaddbd

                    abc_cbf cbaddb
                    bac_bf baddb
            ac_bf addb                       bac_f add
                        
                


We know that the size of target has to be the size left + size right

if both strings are empty, return 0 if there is target left
if both and target, return 1
Look at the first chars, if one of them matches, recurse with the rest
if both matches, return the recursion of one or the other 
if none work, return 0


O(2^n) time complexity where n is the size of the target
O(n^2) space where n is the size of the target

"""
class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, left: str, right: str, 
                     target: str) -> int:
        if not left and not right:
            return int(len(target) == 0)
        if not target:
            return 0
        is_interleave: int = 0
        if left and left[0] == target[0]:
            is_interleave = self.isInterleave(left[1:], right, 
                                              target[1:])
        if right and right[0] == target[0]:
            is_interleave = (
                is_interleave or 
                self.isInterleave(left, right[1:], target[1:])
            )
        return is_interleave



