import unittest


def one_away(first: str, second: str) -> bool:
    if (len(first) > len(second) + 1 or
        len(second) > len(first) + 1):
        return False
    if len(first) == len(second):
        return one_away_same_size(first, second)
    else:
        return one_away_diff_size(first, second)


def one_away_diff_size(first: str, second: str) -> bool:
    bigger: str = first if len(first) > len(second) else second
    smaller: str = second if len(first) > len(second) else first
    diff: int = 0 
    i, j = 0, 0
    while i < len(bigger) and j < len(smaller):
        if bigger[i] == smaller[j]:
            j += 1
            i += 1
        else:
            diff += 1
            i += 1
            if diff > 1:
                return False
    return True


def one_away_same_size(first: str, second: str) -> bool:
    diff: int = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            diff += 1
    return diff <= 1


class Test(unittest.TestCase):

    def test(self):
        data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
        ]
        for test_s1, test_s2, expected in data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)


unittest.main()
