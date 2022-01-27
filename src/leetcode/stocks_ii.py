"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.

You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


In - prices: List[int]
Out - int


at each step we can
    buy, sell, do nothing

                                
                                1 2 3
                b1                              _
        s1              _               b2              _
    b3      _       b3      _       s2      _           

keep track of profit trying selling, buying and skipping
max_profit = max(max_profit, solve(prices, start, bought_index))
remember that we cant buy if sold, and cant sell if not bought
memoization here is the start_index and the bought_index

O(n^2) time where n is the size of the list
O(n) space 
"""
from typing import List, Tuple, Dict, Optional


Cache = Dict[Tuple[int, Optional[int]], int]

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, prices: List[int]) -> int:
        cache: Cache = dict()
        return self.find_max(prices, start=0, bought=None, cache=cache)

    def find_max(self, prices: List[int], start: int, 
                 bought: Optional[int], cache: Cache) -> int:
        if start >= len(prices):
            return 0
        if (start, bought) in cache:
            return cache[(start, bought)]
        max_profit: int = 0
        # 1 2 3
        for index in range(start, len(prices)):
            if bought is not None:
                # Sells
                max_profit = max(
                    max_profit, 
                    (prices[index] - prices[bought] + 
                     self.find_max(prices, start+1, None, cache))
                )
            
            # Buys
            max_profit = max(
                max_profit, 
                self.find_max(prices, start+1, index, cache)
            )
        cache[(start, bought)] = max_profit
        return cache[(start, bought)]
            
"""
Alternative

1 2 3 


        3
    2   
1

we want to buy at a valley and sell at a peak
    identify by looking sliding window of three and looking the mid as the smallest/bigger value
when we see a valley, we buy 
iterate on the array, keeping a last and looking ahead
keep a bought: Optional[int]
    if bought is None we do not sell
keep a profit: int
last starts as infinite and add -inf at the end of the list (iterate until -1)

"""
import sys
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        prices.append(-sys.maxsize)  # Ask before if we can change it
        profit: int = 0
        bought: Optional[int] = None
        for i, price in enumerate(prices[:-1]):
            # It does not metter that you can buy at the same time, 
            # cuz its the same of not selling
            if bought is None:
                if self.is_valley(price, prices[i+1]):
                    bought = price
            else:
                if self.is_peak(price, prices[i+1]):  # TODO
                    profit += price - bought
                    bought = None
        return profit

    def is_peak(self, mid: int, right: int) -> bool:
        return mid > right

    def is_valley(self, mid: int, right: int) -> bool:
        return mid < right
        

