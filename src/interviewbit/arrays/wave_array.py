"""
Given an array of integers A, sort the array into a wave like array and return it, In other words, arrange the elements into a sequence such that

a1 >= a2 <= a3 >= a4 <= a5.....

NOTE : If there are multiple answers possible, return the one that's lexicographically smallest.


6 2 9 8 12 10

2 8 9 6 12 1 10
8 2 9 6 12 1 10


12 2 6 8 10 9
2 12 6 8 10 9


iterate jumping two with a for loop till -1
make the swaps 
    three swap
    twos swap


O(n) time complexity 
O(n) space where n is the size of the list

2 1 4 3 6 5 7

2 1 3

In - numbers: List[int]
Out - List[int]

"""
from typing import List


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, numbers: List[int]) -> List[int]:
        last_position: int = len(numbers) - 1
        for window_start in range(0, len(numbers) - 1, 2):
            window_end: int = min(window_start + 2, last_position)
            self.swap_window(numbers, window_start, window_end)
        return numbers

    def swap_window(self, numbers: List[int], 
                    start: int, end: int) -> None:
        # Case of the window size of one
        if end - start == 1 and numbers[end] > numbers[start]:
            numbers[end], numbers[start] = numbers[start], numbers[end]
        mid: int = start + 1
        # Checks to see if it needs fixing
        if end - start == 2 and numbers[mid] != min(numbers[start:end+1]):
            swap_index: int = start if numbers[start] < numbers[end] else end
            numbers[swap_index], numbers[mid] = (numbers[mid], 
                                                 numbers[swap_index])


            

