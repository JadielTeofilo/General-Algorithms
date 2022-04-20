"""
Problem Description

Given a string A denoting a stream of lowercase alphabets. You have to make new string B.

B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found then append '#' at the end of B.


A = "abadbc"

a
ab
aba
abad


keep a set and a list

a {a} 
ab {ab}
ba {a2b1}
bad {a2b1d1}

Input 2:

 A = "abcabc"



Example Output

Output 1:

 "aabbdd"

Output 2:

 "aaabc#"


we iterate on the stream, keeping a count of each char
we keep a queue to be able to know the right char to insert at a given point
at each iter we popleft if it has more then one element 


O(n) time complexity where n is the size of the input
O(n) space complexity


"""
import collections
from typing import Deque, List, Dict


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, chars: str) -> str:
        result: List[str] = []
        deque: Deque[str] = collections.deque()
        counter: Dict[str, int] = collections.defaultdict(int)
        for char in chars:
            deque.append(char)
            counter[char] += 1
            while deque and counter[deque[0]] > 1:
                deque.popleft()
            result.append(deque[0] if deque else '#')
        return ''.join(result)
        



