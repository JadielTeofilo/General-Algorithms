"""
You are given an array A consisting of strings made up of the letters 'a' and 'b' only.
Each string goes through a number of operations, where:

1.  At time 1, you circularly rotate each string by 1 letter.
2.  At time 2, you circularly rotate the new rotated strings by 2 letters.
3.  At time 3, you circularly rotate the new rotated strings by 3 letters.
4.  At time i, you circularly rotate the new rotated strings by i % length(string) letters.



Eg: String is "abaa"


     At time 1, string is "baaa", as 1 letter is circularly rotated to the back

     At time 2, string is "aaba", as 2 letters of the string "baaa" is circularly rotated to the back

     At time 3, string is "aaab", as 3 letters of the string "aaba" is circularly rotated to the back

     At time 4, string is again "aaab", as 4 letters of the string "aaab" is circularly rotated to the back

     At time 5, string is "aaba", as 1 letters of the string "aaab" is circularly rotated to the back

After some units of time, a string becomes equal to its original self.
Once a string becomes equal to itself, it's letters start to rotate from the first letter again (process resets). So, if a string takes t time to get back to the original, at time t+1 one letter will be rotated and the string will be its original self at 2t time.
You have to find the minimum time, where maximum number of strings are equal to their original self.
As this time can be very large, give the answer modulo 109+7.

Note: Your solution will run on multiple test cases so do clear global variables after using them.

In - words: List[str]
Out - int


[a, ababa, aba]

discorver the life value for each string
rotate the string by removing the first element and appending at the end

abab
abab

vabvab
bvabvabva

1212121212

A = (n(n+1))//2
n^2 + n = A * 2
n^2 + n - A*2 = 0
(-1 +- sqrt(1+4*A*2))/2



iterate on the words
for each word find the min rotations, and then the life
with list of life value take the mmd
"""
from typing import List, Iterable


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, words: List[str]) -> int:
        if not words: 
            return 0 
        rotations: Iterable[int] = self.find_rotations(words)
        lives: Iterable[int] = self.find_lives(rotations)
        result: int = 1
        for life in lives:
            result = self.get_lcm(result, life)
        return result % 1000000007

    def find_rotations(self, words: List[str]) -> Iterable[int]:
        for word in words:
            lps: List[int] = self.get_lps(word)
            if len(word) % (len(word) - lps[-1]) == 0:
                yield len(word) - lps[-1]
            else:
                yield len(word)

    def get_lps(self, word: str) -> List[int]:
        lps: List[int] = [0] * len(word)
        i, j = 0, 1
        while j < len(word):
            if word[i] == word[j]:
                lps[j] = lps[j-1] + 1
                i += 1
            else:
                while i != 0 and word[i] != word[j]:
                    i -= 1
            j += 1
        return lps
        
    def find_lives(self, rotations: Iterable[int]) -> Iterable[int]:
        for rotation in rotations: 
            for num in range(1, 2*rotation+1):
                if (num*(num+1))/2 % rotation == 0:
                    yield num
                    break

    def get_lcm(self, left: int, right: int) -> int:
        return abs(left * right) // self.get_gcd(left, right)

    def get_gcd(self, left: int, right: int) -> int:
        if right > left:
            return self.get_gcd(right, left)
        if right == 0:
            return left
        return self.get_gcd(right, left % right)

