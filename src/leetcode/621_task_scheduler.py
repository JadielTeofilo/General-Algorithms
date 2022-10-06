"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.


Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.


A: 4

R: 3
B: 3
C: 3



ABCZABCZABCZ


CARBARBARBAC AC  


ABCA  A

max possible idle (num of most frequent - 1) * n = 4*2 = 8
After that We go over the most frequents, subtracting from the idle time (min(max_freq-1, curr))

result is len(tasks) + idle time

Hi @lubiflash Only if the frequency of "B", "C" and "D" is not greater than "A". The first solution should work. Thinking about the idle_time = (f_max - 1) * n is under control of the cool down period. In this case, we can just down the idle time to zero when we iterate "B". Because "B" just fill up the idle time holes between As. (the last 'B' is after the last 'A'). So for the remaining part of "C". we can insert them one by one to every interval between As which of course will not break the cooling down policy. And also "D" is. So CPU would not have new idle time. So the result is the length of tasks. Hope this is helpful.



"""
import collections
from typing import Dict



class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter: Dict[str, int] = collections.Counter(tasks)
        frequencies: List[int] = list(
            sorted(counter.values(),
                   reverse=True)
        )
        max_frequency: int = frequencies[0]
        idle_time: int = (max_frequency - 1) * n
        for index in range(1, len(frequencies)):
            idle_time -= min(max_frequency - 1, frequencies[index])
            if idle_time <= 0:
                break
        return len(tasks) + max(0, idle_time)


