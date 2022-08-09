"""
You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

1 First clarification

1 <= tasks size < 
-10<= tasks[i] < 10


2 Understance examples

2 2 2 2 2 2 1 1
0 1 0 2 1 1 0 2


1 2

Have a counter for the elements


check < 3
2: 6  # %3 == 0 so add //3 to result
3: 7  # val-2 %3 or val - 4 %3
4: 5  # 3*2 + 1


3*k
or
3*k + 1 = 3*(k-1) + 4
or 
3*k + 2

When we are thinking of multiples of a number, say 3 you can think of the mod of 3:
    0 1 2 0 1 2 0 1 2
or think of a 3-nary number each bit can take 3 values. 
The point is that it goes 3 by three, and to access ANY value all you have to do is +1 or +2


O(n) time complexity where n is the size of tasks
O(n) space complexity 


""" 
import collections
from typing import List, Dict


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter: Dict[int, int] = collections.Counter(tasks)
        result: int = 0
        for count in counter.values():
            if count < 2:
                return -1
            if count % 3 == 0:
                result += count // 3
            else:
                result += count // 3 + 1
        return result

