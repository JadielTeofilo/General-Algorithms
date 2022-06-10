"""
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

    When you get an instruction 'A', your car does the following:
        position += speed
        speed *= 2
    When you get an instruction 'R', your car does the following:
        If your speed is positive then speed = -1
        otherwise speed = 1
    Your position stays the same.

For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.


Let's say n is the length of target in binary and we have 2 ^ (n - 1) <= target < 2 ^ n
We have 2 strategies here:

1. Go pass our target , stop and turn back
We take n instructions of A.
1 + 2 + 4 + ... + 2 ^ (n-1) = 2 ^ n - 1
Then we turn back by one R instruction.
In the end, we get closer by n + 1 instructions.

2. Go as far as possible before pass target, stop and turn back
We take n - 1 instruction of A and one R.
Then we take m instructions of A, where m < n

Consider two general cases for number i with bit_length n.

1    i==2^n-1, this case, n is the best way
2    2^(n-1)-1<i<2^n-1, there are two ways to arrive at i:
        Use n A to arrive at 2^n-1 first, then use R to change the direction, by here there are n+1 operations (n A and one R), then the remaining is same as dp[2^n-1-i]
        Use n-1 A to arrive at 2^(n-1)-1 first, then R to change the direction, use m A to go backward, then use R to change the direction again to move forward, by here there are n-1+2+m=n+m+1 operations (n-1 A, two R, m A) , current position is 2^(n-1)-1-(2^m-1)=2^(n-1)-2^m, the remaining operations is same as dp[i-(2^(n-1)-1)+(2^m-1)]=dp[i-2^(n-1)+2^m)].




For target we can hit it in n A steps if t == 2^n - 1, otherwise we have a window 2^(n-1)-1 to 2^n - 1 to search for. you can go to 2^n -1, add R and solve(diff), or you can go to 2^(n-1)-1, add R, test all diff As, add R and solve(diff), remember to memoize

"""
import sys
from typing import Dict


class Solution:

    def __init__(self):
        self.cache: Dict[int, int] = {}

    def racecar(self, target: int) -> int:
        n = target.bit_length()
        if target in self.cache:
            return self.cache[target]
        if 2 ** n - 1 == target:
            self.cache[target] = n
            return self.cache[target]
        min_path: int = self.racecar(2**n - 1 - target) + n + 1
        for reverse in range(n - 1):
            min_path = min(
                min_path, 
                self.racecar(target - ((2**(n-1)-1) - (2**reverse-1))) + reverse + 2 + n - 1
            )
        self.cache[target] = min_path
        return min_path

