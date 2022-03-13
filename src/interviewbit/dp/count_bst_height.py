"""
You are given two positive integers A and B. For all permutations of [1, 2, …, A], we create a BST. Count how many of these have height B.

Notes:

    Values of a permutation are sequentially inserted into the BST by general rules i.e in increasing order of indices.
    Height of BST is maximum number of edges between root and a leaf.
    Return answer modulo 109 + 7.
    Expected time complexity is worst case O(N4).
    1 ≤ N ≤ 50


                    pick 1 to N
  1 to i - 1 and i + 1 to N

  the recursion will return the number of ways that we get a height of target
  



"""
from typing import List, Dict, Tuple


Cache = Dict[Tuple[int, int, int], int]

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cntPermBST(self, number: int, target: int) -> int:
        cache: Cache = {}
        return self.max_height(start=1, end=number+1, cache=cache, 
                               target=target+1)

    def max_height(self, start: int, end: int, target: int, cache: Cache) -> int:
        if end - start <= 0:
            return int(target == end - start)  # 1 if true 0 otherwise
        if target == 0:
            return 0

        if (start, end, target) in cache:
            return cache[(start, end, target)]
        ways = 0
        for i in range(start, end):
            left_nums: int = self.max_height(start=start, end=i, 
                                             target=target-1, cache=cache)
            right_nums: int = self.max_height(start=i+1, end=end, 
                                              target=target-1,cache=cache)
            if left_nums == 0 and right_nums == 0:
                continue
            # Adds the product beween ways from left and right 
            # and defaults a side to one so it wont make it always 0
            ways += (left_nums or 1) * (right_nums or 1)
        cache[(start, end, target)] = ways
        return ways
            
 
