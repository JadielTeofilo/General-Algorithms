"""

in:

List[List[int]]

out:

List[List[int]]

1 0 1 2
2 3 0 1 
0 2 2 0
2 0 1 1



"""
from typing import List, Optional
import unittest


def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
	if not matrix or not matrix[0]:
		return matrix
	zeros_on_first_row: bool = there_is_zero_on_row(matrix=matrix, row=0)
	zeros_on_first_column: bool = there_is_zero_on_column(matrix=matrix, column=0)
	
	# Set zero on first element of row when there is a zero on the row. Same for column
	for row in range(1, len(matrix)):
		for column in range(1, len(matrix[row])):
			if matrix[row][column] == 0:
				matrix[0][column] = 0
				matrix[row][0] = 0


	set_zeros_based_on_first_element(matrix)
	if zeros_on_first_row:
		set_zeros(matrix=matrix, target_row=0)
	if zeros_on_first_column:
		set_zeros(matrix=matrix, target_column=0)

	return matrix


def there_is_zero_on_row(row: int, matrix: List[List[int]]) -> bool:
	return bool([item for item in matrix[row] if item == 0])


def there_is_zero_on_column(column: int, matrix: List[List[int]]) -> bool:
	has_zero: bool = False
	for row in range(len(matrix)):
		has_zero = True if matrix[row][column] == 0 else has_zero
	return has_zero


def set_zeros_based_on_first_element(matrix: List[List[int]]) -> None:
	""" Sets zero on a element if the first element on its row or first element 
		on its column is zero """	

	for row in range(len(matrix)):
		for column in range(len(matrix)):
			if matrix[0][column] == 0 or matrix[row][0] == 0:
				matrix[row][column] = 0


def set_zeros(matrix: List[List[int]], target_row: Optional[int] = None, target_column: Optional[int] = None) -> None:
	
	for row in range(len(matrix)):
		if target_column is None:
			break
		matrix[row][target_column] = 0
	for column in range(len(matrix[0])):
		if target_row is None:
			break
		matrix[target_row][column] = 0


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
	
	
