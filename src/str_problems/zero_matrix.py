from typing import List, Set
import unittest
import collections


Spot = collections.namedtuple('spot', ['line', 'column'])


def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not matrix[0]:
        return matrix
    spots_with_zeros: List[Spot] = find_zeroed_spots(matrix)
    for spot_with_zero in spots_with_zeros:
        set_zeros(spot_with_zero.line, spot_with_zero.column, matrix)
    return matrix


def find_zeroed_spots(matrix: List[List[int]]) -> List[Spot]:
    result: List[Spot] = []
    for line in range(len(matrix)):
        for col in range(len(matrix[line])):
                if matrix[line][col] == 0:
                    result.append(Spot(line, col))
    return result


def set_zeros(line, column, matrix):
    for moving_line in range(len(matrix)):
        matrix[moving_line][column] = 0
    for moving_column in range(len(matrix[line])):
        matrix[line][moving_column] = 0


class Test(unittest.TestCase):
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




if __name__ == '__main__':
    unittest.main()
