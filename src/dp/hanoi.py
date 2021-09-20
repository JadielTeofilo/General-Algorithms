"""
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (Le., each disk sits on top of an even larger one). You have the following
constraints:
    
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using Stacks.

"""
from typing import List
import collections
import dataclasses


LEFT = 0
MID = 1
RIGHT = 2


Towers = collections.namedtuple('Towers', 'left mid right')


@dataclasses.dataclass
class Tower:
    
    stack: List[int] = dataclasses.field(default_factory=list)
    
    def insert(self, value: int) -> None:
        """ Verifies the constraints and 
            inserts to stack """
        if self.stack and self.peek() < value:
            raise ValueError('Tower can not take in bigger value')
        self.stack.append(value)
        
    def pop(self) -> int:
        return self.stack.pop()
    
    def empty(self) -> bool:
        return not self.stack
    
    def peek(self) -> int:
        if self.empty():
            raise IndexError('Empty tower')
        return self.stack[-1]   


@dataclasses.dataclass
class HanoiTower:
    towers: Towers = dataclasses.field(
        default_factory=lambda: Towers(Tower(), Tower(), Tower())
    )
    
    def move_block(self, block: int, origin: int, target: int, 
                   buffer: int) -> None:
        """ Moves the requested block to the requested tower """
        if block == 0:
            return 
        
        self.move_block(block - 1, origin, buffer, target)
        self.move_top(origin, target)
        self.move_block(block - 1, buffer, target, origin)
    
    def move_top(self, origin: int, target: int) -> None:
        self.towers[target].insert(self.towers[origin].pop())
        
    def solve(self) -> None:
        """ Moves all blocks from first tower to last """
        self.move_block(self.towers.left.stack[0], LEFT, RIGHT, MID)


def build_and_test_hanoi(size: int) -> None:
    first_stack: List[int] = [index + 1 for index in range(size)]
    first_stack.reverse()
    hanoi = HanoiTower(Towers(Tower(first_stack), Tower(), Tower())) 
    print(hanoi)
    hanoi.solve()
    print(hanoi)
    
    
if __name__ == '__main__':
    build_and_test_hanoi(1)
    build_and_test_hanoi(5)
    
