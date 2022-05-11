"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

11106
  -
12322

dp[i]
    when num[i-1:i+1] in the range [10, 26] 
        dp[i] = dp[i - 2] if i > 1 else 1
    when num[i] in range [1,9]
        dp[i] += dp[i - 1] if i > 0 else 1

return dp[-1]
    

O(n) time and space complexity where n is the size of the input string

"""
from typing import List


class Solution:
    def numDecodings(self, message: str) -> int:
        if not message:
            return 0
        dp: List[int] = [0] * len(message)
        for i, number in enumerate(message):
            if i > 0 and 10 <= int(message[i - 1: i + 1]) <= 26:
                dp[i] = dp[i - 2] if i > 1 else 1
            if int(number) != 0:
                dp[i] += dp[i - 1] if i > 0 else 1
        return dp[-1]
