"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



The brute force approach

at a given point, three options, buy, sell, do nothing
keep track of the num of operations done
keep bought price

stop when max operaitions reached or end of prices
only sell if bought

max_profit = get_max(prices, start=i+1, bought=None, ops=ops-1)

O(n^2*o) time complexity n is the size of input, o is the operations
O(n) since you will try to go all the way without buying


Better approach


keep a machine state


bought(-price)      ->      sold (+price)        ->      bought(-price)      ->      sold(+price)

sized k*2

the idea is to maximize every step of it, so

states: List[int] = [0] * (k*2)
state[0] = max(state[0], -price)  # Buying
state[1] = max(state[1], state[0] + price)  # Selling

at the end just return the last state

O(k*n) time
O(k) space

"""
import sys
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k <= 0:
            return 0
        states: List[int] = [-sys.maxsize] * (k*2)
        for price in prices:
            last = 0
            signal = -1  # Starts with a buy which removes money
            for i, state in enumerate(states):
                states[i] = max(states[i], last + (price * signal))
                last = states[i]
                signal *= -1  # Flip the signal
        return max(states[-1], 0)


