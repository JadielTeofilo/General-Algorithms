"""
It is an array of length n where the i-th element is equal to the greatest number of characters starting from the position i that coincide with the first characters of the string.
    It also allows for pattern finding in O(m+n). Just concat the pattern to the string = pattern + $ + text. Then take the z function of it and, starting from $ (char not present on text) , return the places that the z function has the size of the pattern.


Explanations https://cp-algorithms.com/string/z-function.html


"""
from typing import List


def z_function(word: str) -> List[int]:
    z: List[int] = [0] * len(word)
    size: int = len(word)
    start, end = 0, 0
    for i in range(1, size):
        if i <= end:  # Case its within the last substring match
            # Means you can just use the z[i - end] which is the last time this value occurred
            z[i] = min(end - i + 1,  # Distance from i to end (max knowlege size we have)
                       z[i - start])
        while i + z[i] < size and word[i + z[i]] == word[z[i]]:
            z[i] += 1
        if i + z[i] - 1 > end:
            start, end = i, i + z[i] - 1
    return z


