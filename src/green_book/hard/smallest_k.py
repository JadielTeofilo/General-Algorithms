"""
Smallest K: Design an algorithm to find the smallest K numbers in an array.


7 2 2 1 1 8 7 9 5
3

R: 1 1 2

1 1 2 2 7 8 7 9 5
          _
1 1 2 2 7 7 5 8 9
1 1 2 2 7 5 7 8 9
1 1 2 2 5 7 7 8 9
1 1 2 2 5 7 7 8 9


In - numbers: List[int], target: int
Out - List[int]


O(n) time complexity where n is the size of numbers
O(1) space complexity since the output is not included

"""
from typing import List


def smallest_k(numbers: List[int], target: int) -> List[int]:
    """
        Uses quick select to find the list of smallest 
        elements on numbers 
    """
    # 2 7 5 9 3 k=2
    # 2 3 5 9 7
    # TODO validate input
    start: int = 0
    end: int = len(numbers) - 1  # 4 

    while start <= end:
        pivot_index: int = (start + end)//2  # 0
        pivot_index = partition(numbers, start, end, pivot_index)
        if pivot_index + 1 == target:
            return numbers[:target]
        if pivot_index + 1 < target:
            start = pivot_index + 1
        else:
            end = pivot_index - 1
    return numbers


def partition(numbers: List[int], start: int, end: int, 
              pivot_index: int) -> int:
    pivot: int = numbers[pivot_index]
    target_list: List[int] = numbers[start:end + 1]
    smaller_numbers: List[int] = [number for number in target_list 
                                        if number < pivot]
    equal_numbers: List[int] = [number for number in target_list 
                                if number == pivot]
    bigger_numbers: List[int] = [number for number in target_list
                                 if number > pivot]
    partitioned_numbers: List[int] = (smaller_numbers + 
                                      equal_numbers +
                                      bigger_numbers)
    # Update the numbers list
    update_index: int = 0
    for i in range(start, end + 1):
        numbers[i] = partitioned_numbers[update_index]
        update_index += 1
    return (start + len(smaller_numbers) 
            + len(equal_numbers) - 1)  # New pivot position


print(smallest_k([7, 2, 2, 2,2,2,2,2,2,21, 1, 1, 8, 7, 9,9,9,9,9,9,9, 5], 14))
