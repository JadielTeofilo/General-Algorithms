"""
Given two integer arrays A and B of size N.

There are N gas stations along a circular route, where the amount of gas at station i is A[i].

You have a car with an unlimited gas tank and it costs B[i] of gas to travel from station i 

to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the minimum starting gas station’s index if you can travel around the circuit once, otherwise return -1.

You can only travel in one direction. i to i+1, i+2, … n-1, 0, 1, 2.. Completing the circuit means starting at i and 

ending up at i again.


In - gas: List[int], cost: List[int]
Out - int


Can we have distance zero?
yes

gas 1 2

cos 2 1


We want to start at the place with the most gas-distance ratio

1 3 2 1 0 0 1 
2 2 1 1 1 1 2

5
6

Use variation of kardane algo

keep a current gas and a last gas, and start index

iterate on the list, curr = gas-cost + last if gas - cost is bigger then curr, update curr, start index 
last updates every time
at the end check if the curr gas allows to get to start 

O(n) time complexity where n is the size of both lists
O(n) space

"""
from typing import List


class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return an integer
	def canCompleteCircuit(self, gas_stations: List[int], 
						   costs: List[int]) -> int:
		if not gas_stations or not costs:
			return -1
		curr: int = 0
		last: int = 0
		start_index: int = 0
		for (index, (gas, cost)) in enumerate(zip(gas_stations, costs)):
			curr = gas - cost + last
			if gas - cost > curr:
				start_index = index
				curr = gas - cost
			last = curr
		return self.check_circuit(gas_stations, costs, start_index)

	def check_circuit(self, gas_stations: List[int], 
					  costs: List[int], start: int) -> int:
		gas_stations = self.rotate(gas_stations, start)
		costs = self.rotate(costs, start) 
		total_gas: int = 0
		for gas, cost in zip(gas_stations, costs):
			total_gas += gas
			total_gas -= cost
			if total_gas < 0:
				return -1
		return start

	def rotate(self, numbers: List[int], start: int) -> List[int]:
		return numbers[start:] + numbers[:start]
		
