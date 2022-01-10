"""
Given a collection of integers that might contain duplicates, S, return all possible subsets.

    Note:

        Elements in a subset must be in non-descending order.
        The solution set must not contain duplicate subsets.
        The subsets must be sorted lexicographically.



If S = [0,1,2,2,2], the solution is:

[
[],
[0]
[1]
[0,1],
[2]
[0,2],
[1,2],
[0,1,2],
]

In - numbers: List[int]
Out - List[List[int]]

"""
import collections
from typing import List, Dict


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, numbers: List[int]) -> List[List[int]]: 
        result: List[List[int]] = [[]]
        visited_count: Dict[int, int] = collections.defaultdict(int)
        for number in numbers:
            self.update_result(
                result, number, 
                visited_count=visited_count
            )
            visited_count[number] += 1
        for subset in result:
            subset.sort()
        result.sort()
        return result

    def update_result(self, result: List[List[int]], 
                      number: int, visited_count: Dict[int, int]) -> None:
        new_values: List[List[int]] = []
        for subset in result:
            counter: Dict[int, int] = collections.Counter(subset)
            # Skips cases where duplicates would be generated
            if number in visited_count:
                curr_amount: int = counter[number]
                if curr_amount < visited_count[number]:
                    continue
            new_values.append(subset + [number])
        result.extend(new_values)


