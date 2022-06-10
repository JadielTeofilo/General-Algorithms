"""
You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}

Note that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.

 

Custom testing:

The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot's position.


0 0 0 0 0 
0 1 0 0 0
0 1 0 0 0
1 0 0 1 0

A bfs or dfs algo variation might be the way

Dfs makes more sense cuz it works in paths, which is possible to the robot to follow

The backtracking has to be done manually

we try moving foward, if not possible, we try right (one turnRight) back (2 Rights) left (3 rights)
look foward again and backtrack (2 right 1 move 2 right)

every try we check against visited before moving

"""
import collections
from typing import Set, List, Optional


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
    pass
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


Position = collections.namedtuple('Position', 'row col')
directions: List[Position] = [Position(-1, 0), Position(0, 1), 
                              Position(1, 0), Position(0, -1)]

class Solution:
    def cleanRoom(self, robot: Robot) -> None:
        """
        :type robot: Robot
        :rtype: None
        """
        visited: Set[Position] = set()
        current: Position = Position(0, 0)
        self.clean_helper(robot, visited, current, 0)

    def clean_helper(self, robot: Robot, visited: Set[Position], 
                     current: Position, direction: int) -> None:
        if current in visited:
            return
        visited.add(current)
        robot.clean()
        for _ in range(4):
            if robot.move():
                new_position: Position = self.get_new_position(current, direction)
                self.clean_helper(robot, visited, new_position, direction)
                self.move_back(robot)
            robot.turnRight()
            direction = (direction + 1) % 4
        
    def get_new_position(self, current: Position, direction: int) -> Position:
        return Position(
            current.row + directions[direction].row, 
            current.col + directions[direction].col
        )

    def move_back(self, robot: Robot) -> None:
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
            
            
                        

