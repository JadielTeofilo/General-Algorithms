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

3 2 5 1   
2 4 2 2

1-2 3-1

5
6

The brute force is to try every starting point, when we get negative, we reset and try another starting point.

The catch is that you dont have to go all the way back and try the start_index + 1, cuz we already know that it wont work given it didn't work with the surplus of the start_index.

We can then, iterate on the input, trying to keep positive, if negative, we reset and try starting from next position. When we get to the last index we continue until we get to start_index - 1


O(n) time complexity where n is the size of both lists
O(1) space

"""
import sys
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        best_index: int = find_best_start(gas, cost)
        if can_loop(best_index, gas, cost):
            return best_index
        return -1


def find_best_start(gas: List[int], cost: List[int]) -> int:
    best_start: int = 0
    current: int = 0
    for index, (gas_item, cost_item) in enumerate(zip(gas, cost)):
        current += gas_item - cost_item
        if current < 0:
            current = 0
            best_start = index + 1
    return best_start

def can_loop(start: int, gas: List[int], cost: List[int]) -> bool:
    initial_path: int = gets_to_the_end(start, len(gas), gas, cost)
    return gets_to_the_end(0, start, gas, cost, initial_path) >= 0


def gets_to_the_end(start: int, end: int, gas: List[int],
                    cost: List[int], current: int = 0) -> int:
    for i in range(start, end):
        current += gas[i] - cost[i]
        if current < 0:
            break
    return current
