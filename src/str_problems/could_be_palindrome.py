import collections 
from typing import Dict
import unittest


def could_be_palindrome(sentence: str) -> bool:
        if not sentence:
            return False
        sentence = remove_spaces(sentence)
        sentence = sentence.lower()
        count: Dict[str, int] = count_letters(sentence)
        odd: int = 0  # Amount of letters with odd count
        for letter in count: 
            if count[letter] % 2 != 0:
                odd += 1
            if odd > 1:
                return False
        return True


def remove_spaces(sentence: str) -> str:
    return sentence.replace(' ', '')


def count_letters(sentence: str) -> Dict[str, int]:
    counter: Dict[str, int] = collections.defaultdict(int)
    for char in sentence:
        counter[char] += 1
    return counter


class Test(unittest.TestCase):

    def test_could_be_palindrome(self):
        data = [    
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]
        for string, result in data:
            self.assertEqual(could_be_palindrome(string), result)


if __name__ == '__main__':
    unittest.main()
