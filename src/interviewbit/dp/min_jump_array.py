"""
Given an array of non-negative integers, A, of length N, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Return the minimum number of jumps required to reach the last index.

If it is not possible to reach the last index, return -1.

Input Format:

The first and the only argument contains an integer array, A.

Output Format:

Return an integer, representing the answer as described in the problem statement.

1 0 1
    0
r = 1

2 3 1 1 4
2 1 2 1 0
2 2 2 1 0

r = 2

fill the last element as 0
iterate backwards on the input building dp array
if num is zero, just put infinite 
check if the min is infinite, if so, just put infinite
dp[i] = 1 + min(dp[i+1:i+num[i]+1])

if first is inf return -1
return first element


O(n^2) time complexity
O(n) space complexity

Greedy 
We can iterate over all indices maintaining the furthest reachable position from current index - maxReachable and currently furthest reached position - lastJumpedPos. Everytime we will try to update lastJumpedPos to furthest possible reachable index - maxReachable.

Updating the lastJumpedPos separately from maxReachable allows us to maintain track of minimum jumps required. Each time lastJumpedPos is updated, jumps will also be updated and store the minimum jumps required to reach lastJumpedPos (On the contrary, updating jumps with maxReachable won't give the optimal (minimum possible) value of jumps required).

We will just return it as soon as lastJumpedPos reaches(or exceeds) last index.

keep global_max and local_max and result
only update global max when ifs smaller then the index then update result
iterate on it 


"""
import math
from typing import List, Union


class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, numbers: List[int]) -> int:
        dp: List[Union[int, float]] = [0] * len(numbers)
        for i in range(len(numbers) - 2, -1, -1):
            # Gets the min from the positions that it can reach
            right_min: Union[float, int] = (min(dp[i+1:i+numbers[i]+1]) 
                                            if numbers[i] > 0 else math.inf)
            if right_min == math.inf:
                dp[i] = math.inf
            else:
                dp[i] = right_min + 1
        if dp[0] == math.inf:
            return -1
        return int(dp[0])

    def jump_greedy(self, numbers: List[int]) -> int:
        if not numbers:
            return -1
        global_max: int = numbers[0]
        local_max: int = numbers[0]
        result = 1
        # 2 1 2 1 0
        # 2 2 4 4 
        # 2 2 2 4
        for i in range(1, len(numbers) - 1):
            local_max = max(local_max, i + numbers[i])
            if global_max == i:
                result += 1
                global_max = local_max
            if global_max <= i:
                return -1
        return result

