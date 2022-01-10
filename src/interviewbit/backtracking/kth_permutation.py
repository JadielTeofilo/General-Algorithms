"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,

We get the following sequence (ie, for n = 3 ) :

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the kth permutation sequence.

For example, given n = 3, k = 4, ans = "231"


1 2 3

                                1 2 3
                1                               2
        2               3           1                       3
3                   2           3                       1


O(k*n^2) time complexity since you ll have k leafs on the three
O(n) space complexity



take the group
number 3 
sequence 2
group = number - 1 // (sequence - 1)! = 
rest = number - 1 % (sequence - 1)!
with 1 at beginning you can generate (n - 1)! sets
1 2 3
1 3 2


solve(numbers: List[int], curr: List[str], sequence: Dict[str, int])


"""
import math
from typing import List, Dict, Optional


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, number: int, sequence_num: int, 
                       curr: str = '', numbers: Optional[List[int]] = None
    ) -> str:
        if numbers is None:
            numbers = [num for num in range(1, number+1)] 
        if not numbers:
            if sequence_num == 0:
                return curr
            return ''
        if sequence_num == 0:
            if numbers:
                curr += ''.join([str(num) for num in numbers])
            return curr
        target_group: int = (sequence_num-1) // math.factorial(number - 1) + 1
        sequence_num = (sequence_num-1) % math.factorial(number - 1)
        numbers: List[int] = [num for num in numbers if num != target_group]
        return self.getPermutation(
            number, sequence_num, curr=curr+str(target_group), numbers=numbers
        )

