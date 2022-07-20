"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.



piles: List[int]
hours: int


k = 4
start = 1
end = max(piles)

if we use binary search (bisect left)
O(p*log(max))

h = 5 -> 7
h = 6 -> 

1 3 5 2 7
1 1 2 1 2 = 7 hours

"""
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles) + 1
        while start < end:
            mid: int = (start + end) // 2
            if can_eat(piles, mid, h):
                end = mid
            else:
                start = mid + 1
        return start


def can_eat(piles: List[int], speed: int, limit: int) -> bool:
    hours_spent: int = 0
    for bananas in piles:
        hours_spent += (bananas // speed)
        if bananas % speed > 0: 
            hours_spent += 1
    return hours_spent <= limit

