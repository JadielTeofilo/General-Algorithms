from typing import List
import unittest


def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or len(matrix) < 2:
        return matrix
    swap_on_diagonal(matrix)
    reverse_lines(matrix)
    return matrix


def swap_on_diagonal(matrix: List[List[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_lines(matrix: List[List[int]]) -> None:
    for line in matrix:
        line.reverse()


class Test(unittest.TestCase):

    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
