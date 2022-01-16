"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

x = target - d

{
target - d: d
}
    Note:

            Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
                    The solution set must not contain duplicate quadruplets.

                    Example : 

                    Given array S = {1 0 -1 0 -2 2}, and target = 0

                    A solution set is:

                        (-2, -1, 1, 2)
                            (-2,  0, 0, 2)
                                (-1,  0, 0, 1)

                                Also make sure that the solution set is lexicographically sorted.

                                Solution[i] < Solution[j] iff Solution[i][0] < Solution[j][0] OR (Solution[i][0] == Solution[j][0] AND ... Solution[i][k] < Solution[j][k])



In - target: int, numbers: List[int]
Out - List[List[int]]

brute force
iterate on the n^4 combinations


6 5 2 1 3
_ _   _   _
n n-1 n-2 n-3

iterate on the list
    iterate on the list
        iterate on the list
            
------
two sum idea
target 3
target - number: number
2: [1]
have a hash 


6 5 2 1 3
    5 2 1 3
        2 1 3



"""
import collections
from typing import Dict, List, Set


Node = collections.namedtuple('Node', 'index value')
Cache = Dict[int, List[Node]]


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, numbers: List[int], target: int) -> List[List[int]]:
        numbers.sort()
        cache: Cache = self.build_twosum_cache(numbers, target)
        result: List[List[int]] = []
        for a in range(len(numbers)):
            if a + 1 < len(numbers) and numbers[a] == numbers[a + 1]:
                continue
            for b in range(a + 1, len(numbers)):
                if b + 1 < len(numbers) and numbers[b] == numbers[b + 1]:
                    continue
                for c in range(b + 1, len(numbers)):
                    if c + 1 < len(numbers) and numbers[c] == numbers[c + 1]:
                        continue
                    aux: int = numbers[a] + numbers[b] + numbers[c]
                    if aux not in cache:
                        continue
                    for index, value in cache[aux]:
                        # Checks for reusage of numbers
                        if index in {a, b, c}:
                            continue
                        result.append(sorted([numbers[a], numbers[b],
                                       numbers[c], value]))
        return sorted(result)

    def build_twosum_cache(self, numbers: List[int], 
                           target: int) -> Cache:
        cache: Cache = collections.defaultdict(list)
        for index, number in enumerate(numbers):
            cache[target - number].append(Node(index, number))
        return cache




