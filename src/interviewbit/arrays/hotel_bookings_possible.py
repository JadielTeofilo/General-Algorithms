"""
Problem Description

A hotel manager has to process N advance bookings of rooms for the next season. His hotel has C rooms. Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .


Input Format

First argument is an integer array A containing arrival time of booking.

Second argument is an integer array B containing departure time of booking.

Third argument is an integer C denoting the count of rooms.


Output Format

Return True if there are enough rooms for N bookings else return False.

Return 0/1 for C programs.

In - arrival: List[int], departure: List[int], rooms: int
Out bool

Its a range problem, sort both lists and iterate on them both, keeping track of num of guests
always iterate on the one with the smaller time

Handle what happens when both have the same time


"""
from typing import List


class Solution:
	# @param arrive : list of integers
	# @param depart : list of integers
	# @param K : integer
	# @return a boolean
	def hotel(self, arrive: List[int], 
			  depart: List[int], rooms: List[int]) -> bool:
		arrive.sort()
		depart.sort()
		guests: int = 0
		i, j = 0, 0
		while i < len(arrive) and j < len(depart):
			if arrive[i] < depart[j]:
				guests += 1
				i += 1
			else:
				guests -= 1
				j += 1
			if guests > rooms:
				return False
		return True
			

