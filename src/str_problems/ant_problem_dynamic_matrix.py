# ant_thing
import dataclasses
import enum
from typing import List
import unittest


class Direction(enum.Enum):
    right = 0
    down = 1
    left = 2
    up = 3


@dataclasses.dataclass
class Position:
    row: int = 0
    column: int = 0

    def move(self, direction: Direction) -> None:
        if direction == Direction.right:
            self.column += 1
        elif direction == Direction.left:
            self.column -= 1
        elif direction == Direction.down:
            self.row += 1 
        elif direction == Direction.up:
            self.row -= 1


@dataclasses.dataclass
class Ant:
    position: Position = Position()
    direction: Direction = Direction.right

    def move(self) -> None:
        self.position.move(self.direction)
            

    def flip(self, side: int) -> None:
        """ Flips direction 90 degree to right (side=1) or left (side=-1) """
        self.direction = Direction((self.direction.value + side) % 4)

@dataclasses.dataclass
class Grid:
    
    matrix: List[List[int]] = dataclasses.field(default_factory=lambda: [[0]])

    def update_matrix_size(self, position: Position) -> Position:
        if position.row >= len(self.matrix) or position.row < 0:
            new_row_count = len(self.matrix) * 2
            old_matrix:  List[List[int]] = self.matrix
            self.matrix = [[0 for _ in range(len(old_matrix[0]))] for _ in range(new_row_count)]
            row_offset: int = len(old_matrix) if position.row < 0 else 0
            self.copy_old_values(old_matrix, row_offset=row_offset)
            position.row += row_offset
        elif position.column >= len(self.matrix[0]) or position.column < 0:
            new_column_count = len(self.matrix[0]) * 2
            old_matrix: List[List[int]] = self.matrix
            self.matrix = [[0 for _ in range(new_column_count)] for _ in range(len(old_matrix))]
            column_offset: int = len(old_matrix[0]) if position.column < 0 else 0
            self.copy_old_values(old_matrix, column_offset=column_offset)
            position.column += column_offset
        return position

    def copy_old_values(self, old_matrix: List[List[int]], 
                                  column_offset: int = 0, 
                                   row_offset: int = 0) -> None:
        for row in range(len(old_matrix)):
            for column in range(len(old_matrix[0])):
                self.matrix[row + row_offset][column + column_offset] = old_matrix[row][column]

    def flip_value(self, position: Position) -> None:
        curr_value: int = self.matrix[position.row][position.column]
        self.matrix[position.row][position.column] = (curr_value + 1) % 2
                    

def print_k_moves(k: int) -> List[List[int]]:
    grid: Grid = Grid()
    ant: Ant = Ant()
    while k > 0:
        k -= 1
        make_a_move(ant, grid)
    return grid.matrix


def make_a_move(ant: Ant, grid: Grid) -> None:
    current_grid_value = grid.matrix[ant.position.row][ant.position.column]
    ant.flip(1 if current_grid_value == 0 else -1)  # flip direction according to grid value
    grid.flip_value(ant.position)
    ant.move()
    ant.position = grid.update_matrix_size(ant.position)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual([[0, 0],[0,0],[1,0],[1,1]], print_k_moves(5))


if __name__ == '__main__':
    import pdb;pdb.set_trace()
    unittest.main()

