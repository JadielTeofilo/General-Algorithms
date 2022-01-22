"""
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.

In number: int
Out - int

Each coin can appear amount/coin_value + 1 times

amount = 100

25 cents can appear either 0, 1, 2, 3 or 4 times

O(n*n) where n is amount, 


"""
from typing import Dict
import collections


COIN_TYPES = [25, 10, 5, 1]
CacheKey = collections.namedtuple('CacheKey', 'amount index')
Cache = Dict[CacheKey, int]


def make_change(amount: int) -> int:
	""" 
		Finds the number of different ways of 
		summing up to amount with the COIN TYPES
	"""
	cache: Cache = {}
	return change_helper(amount, 0, cache)


def change_helper(amount: int, index: int, 
				  cache: Cache) -> int:

	# On the last coin just return 1 cuz there is only one way of using it
	if index >= len(COIN_TYPES) - 1:  
		return 1
	if cache.get(CacheKey(amount, index)):
		return cache[CacheKey(amount, index)]
	curr_coin: int = COIN_TYPES[index]
	# Number of the curr coin that can be used 
	# to sum up to amount
	max_coin_number: int = amount // curr_coin
	ways: int = 0
	for coin_number in range(max_coin_number + 1):
		remainder: int = amount - curr_coin * coin_number
		ways += change_helper(remainder, 
							  index + 1, 
							  cache)
	cache[CacheKey(amount, index)] = ways
	return ways


print(make_change(1))
print(make_change(10))
print(make_change(20))
import pdb;pdb.set_trace()
