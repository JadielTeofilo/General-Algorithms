"""
in str, str

out bool


waterbottle

erbottlewaterbottlewatter

bac

acbacb


"""
import unittest


def is_substring(sub_string: str, string: str) -> bool:
	return sub_string in string


def is_rotation(string: str, rotated_string: str) -> bool:
	if len(rotated_string) != len(string):
		return False
	expanded_string: str = rotated_string + rotated_string
	return is_substring(string, expanded_string)


class Test(unittest.TestCase):
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = is_rotation(s1, s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

