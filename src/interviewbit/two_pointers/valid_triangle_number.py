"""
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.



a triangle is valid if the sides a, b and c are so that:

a + b > c, b + c > a and a + c > b

if se sort it we know that a <= b <= c and so, a + c > b and b + c > a will always be true a (since c is bigger equal then both of them)



iterate on the sorted numbers with pointer i and j
the k has to be found for the triplet to be formed

binary search is possible 
the sorted option lets us not reset k to j + 1 at each step


O(n^2) time
O(n) space depending on the implementation of the sorting algo




"""
from typing import List


class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, numbers: List[int]):
        result: int = 0
        numbers.sort()
        for i in range(len(numbers)):
            k: int = i + 2
            for j in range(i + 1, len(numbers)):
                target_sum: int = numbers[j] + numbers[i]
                while k < len(numbers) and target_sum > numbers[k]:
                    k += 1
                result += (k - j - 1)
        return result


