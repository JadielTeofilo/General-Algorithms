"""

You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array persons of size n, where persons[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

Input: flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.



If you have the starts and ends sorted separetly, for a given time, if you find its position on both the arrays, you will know how many blommed and how many died
        [1, 3, 4, 9]
        [6, 7, 12, 13]

O(p*log(f) + flog(f)) time complexity where f =flowers and p=people
O(f)

It is also possible to use the meeting rooms approach, the one where you build a hash telling the additions and removals, but to avoid using the full range, use a SortedDict

"""
import bisect
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], 
                         people: List[int]) -> List[int]:
        starts: List[int] = sorted([flower[0] for flower in flowers])
        ends: List[int] = sorted([flower[1] for flower in flowers])
        result: List[int] = [0] * len(people)
        for index, person in enumerate(people):
            result[index] = (bisect.bisect_right(starts, person) - 
                             bisect.bisect_left(ends, person))
        return result

