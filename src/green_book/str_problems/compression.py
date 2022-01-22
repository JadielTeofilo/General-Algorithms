from typing import List
import unittest


def compression(word: str) -> str:
    result: List[str] = []
    if not word: 
        return word
    last_visited: str = word[0]
    result.append(word[0])
    count: int = 0
    for char in word:
        if char == last_visited:
            count += 1
        else:
            result.append(str(count))
            result.append(char)
            count = 1
        last_visited = char
    result.append(str(count))
    result: str = ''.join(result)
    return result if len(result) < len(word) else word


class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = compression(test_string)
            self.assertEqual(actual, expected)


unittest.main()
