"""
Problem Description

A message containing letters from A-Z is being encoded to numbers using the following mapping:

 'A' -> 1
 'B' -> 2
 ...
 'Z' -> 26

Given an encoded message A containing digits, determine the total number of ways to decode it modulo 109 + 7.
"""

class Solution:

    def __init__(self):
        super(Solution, self).__init__()
        self.dp = {}

    # @param A : string
    # @return an integer
    def numDecodings(self, encoded):
        if encoded == '0':
            return 0
        if len(encoded) < 2:
            return len(encoded)
        dp = [0] * len(encoded) + [1]
        dp[-2] = self.get_count(encoded[-1])
        for i in range(len(encoded)-2, -1, -1):
            ones_count = 0
            if encoded[i] != '0':
                ones_count = dp[i+1]
            twos_count = 0
            if 10 <= int(encoded[i:i+2]) <= 26:
                twos_count = dp[i+2]
            dp[i] = ones_count + twos_count
        return dp[0] % (10**9 + 7)

    def get_count(self, char):
        return 1 if char != '0' else 0



