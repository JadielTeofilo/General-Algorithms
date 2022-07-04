"""
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.




Its a partition problem but notice that we dont have to pick contiguous elements, which makes the binary search solution weird (with it we would get a size for the partition, but here its hard to validate).

The way to do it is to go backtracking, keep the count of each person


iterate on the people, try giving the curr bag to each of them and call the recursion for the next bag



solve(bags: List[int], start: List[int], people_count: List[int])

we stop when start == len(bags) and return the min of people_count


"""
import sys
from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        return min_cookies(bags=cookies, start=0, people_cookies=[0] * k)


def min_cookies(bags: List[int], start: int,
                people_cookies: List[int]) -> int:
    if start == len(bags):
        return max(people_cookies)
    result: int = sys.maxsize
    for i in range(len(people_cookies)):
        people_cookies[i] += bags[start]
        if people_cookies[i] < result:
            result = min(result, min_cookies(bags, start + 1, people_cookies))
        people_cookies[i] -= bags[start]
    return result
