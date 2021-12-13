"""
Given a string A consisting of lowercase characters.

You have to find the number of substrings in A which starts with vowel and end with consonants or vice-versa.

Return the count of substring modulo 109 + 7.

aabaabbbab

remove non alpha chars
Cache telling how many elements there are of that type to the right
vowel_cache 
consonant_cache 

In - word: str
Out - int mod 10 ** 9 + 7

O(n) time and space where n is the len of the word

"""
import re
from typing import List


VOWELS = {'a', 'e', 'i', 'o', 'u'}


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, word: str) -> int:
        word = re.sub('[^a-z]', '', word)  # Remove non alpha chars
        vowel_cache: List[int] = self.build_cache(word, vowels=True)
        consonant_cache: List[int] = self.build_cache(word, vowels=False)
        result: int = 0
        for index, char in enumerate(word):
            if char in VOWELS:
                result += consonant_cache[index]
                continue
            result += vowel_cache[index] 
            result %= (10**9 + 7)
        return result

    def build_cache(self, word: str, vowels: bool) -> List[int]:
        cache: List[int] = [0] * len(word)
        # Starts the last element
        cache[-1] = self.find_value(word, -1,  vowels)
        for index in range(len(word) - 2,  -1, -1):
            char = word[index]
            cache[index] += cache[index + 1]
            cache[index] += self.find_value(word, index, vowels)
        return cache

    def find_value(self, word: str, index: int, vowels: bool) -> int:
        if ((vowels and word[index] in VOWELS) or
            (not vowels and word[index] not in VOWELS)):
            return 1
        return 0


