from typing import List
import unittest


def urlify(sentence: List[str], true_lenght: int) -> str:
    new_index: int = len(sentence) - 1
    for i in range(true_lenght - 1, -1, -1):
        if sentence[i] != ' ':
            sentence[new_index] = sentence[i]
            new_index -= 1
        else:
            sentence[new_index - 2: new_index + 1] = '%20'
            new_index -= 3
    return ''.join(sentence)


class Test(unittest.TestCase):

    def test_urlify(self):
        expected: str = 'much%20ado%20about%20nothing'
        self.assertEqual(expected, urlify(list('much ado about nothing      '), 22))


if __name__ == '__main__':
    unittest.main()
