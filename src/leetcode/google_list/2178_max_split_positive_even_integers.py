"""

You are given an integer finalSum. Split it into a sum of a maximum number of unique positive even integers.

    For example, given finalSum = 12, the following splits are valid (unique positive even integers summing up to finalSum): (12), (2 + 10), (2 + 4 + 6), and (4 + 8). Among them, (2 + 4 + 6) contains the maximum number of integers. Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.

Return a list of integers that represent a valid split containing a maximum number of integers. If no valid split exists for finalSum, return an empty list. You may return the integers in any order.



12 

2 + 4 + 6

14 

4 6

if even we can just return []


1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
                         -


start, current, final_sum

                           2, [], 12
               4 [2] 10                 4 [] 12


stop when we see final_sum == 0 or start > final_sum

at each step, pick start of skip it, stick to the answer with bigger len

memoize on the start, final_sum

O(n^2) time complexity where n is final size
O(n) space complexity


Better:

Notice what happens when we go over

target = 14

2 4 6  8
2 6 12 20

The idea is that since we are going over, instead of adding a new number, we increase the last number to reach the target already, we do this cuz we wont be able to add another number anyways

O(n) time complexity
O(1) space (not considering the output)

"""
from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        result: List[int] = []
        start: int = 2
        curr_sum: int = 0
        while (curr_sum + start) <= finalSum:
            curr_sum += start
            result.append(start)
            start += 2
        if curr_sum != finalSum:
            result[-1] = result[-1] + (finalSum - curr_sum)
        return result

        

