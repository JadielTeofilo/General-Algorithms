"""
Given any integer, print an English phrase that describes the integer (e.g., "One Thousand, Two Hundred Thirty Four").

in:
int

out:
str

Is there a limit to how big the input is? 32 bit integer?

32 bit integer a most 2 ^ 32 - 1
2 bilhoes


1220440
one million two hundred twenty thousand four hundred forty 
one million two hundred twenty thousand four hundred forty

0 -

4 forty

4 four hundred

0 -

thousand 

2 twenty

2 two hundred


1 million

% 10 

// 10

"""
from typing import Iterator, Dict, List


def english_int(number: int) -> str:
	""" Converts any 32 bit integer value into its string representation"""
	if number == 0:
		return 'zero'

	hundredth_house: int = 0  # values ranging from zero to four (billion)
	unit_house: int = 0  # value ranging from zero to two
	result: List[str] = []

	for digit in reverse_iterate_number(number):
		# Is the first unit of the hundred
		if unit_house == 0:
			result.append(find_correspondent_hundred_string(hundredth_house))
		result.append(find_correspondent_digit_string(digit, unit_house))
		# is the last unit of the hundred
		if unit_house == 2:
			hundredth_house += 1
		unit_house = (unit_house + 1) % 3

	return ' '.join(reversed(result)).replace('ten two', 'twelve').replace('ten one', 'eleven')
		

def reverse_iterate(number: int) -> Iterator:
	""" Returns every digit from number in a reveresed manner """
	while number > 0:
		yield number % 10
		number //= 10


def find_correspondent_digit_string(digit: int, unit_house: int) -> str:
	
	first_unit_digit: Dict[int, str] = {
		0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
	}
	second_unit_digit: Dict[int, str] = {
		0: '', 1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'fourty',
	}

	translation_equivalency: Dict[int, Dict[int, str]] = {
		0: first_unit_digit, 1: second_unit_digit, 2: first_unit_digit,
	}

	return translation_equivalency[unit_house][digit] + ('hundred' if unit_house == 2 else '')


def find_correspondent_hundred_string(hundredth_house: int) -> str:
	return {
		0: '', 1: 'thousand', 2: 'million', 3: 'billion'
	}[hundredth_house]
	

class Test(unittest.TestCase):

	data = ]
		(120, 'one hundred twenty'), 	
		(121, 'one hundred twenty one'), 	
		(1, 'one'), 	
		(1220, 'one thousand two hundred twenty'), 	
		(12202, 'twelve thousand two hundrend two'), 	
		(120202, 'one hundred twenty thousand two hundrend two'), 	
		(1120202, 'one million one hundred twenty thousand two hundrend two'), 	
		(1000120202, 'one billion a hundred twenty thousand two hundrend two'), 	
	]

