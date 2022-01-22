"""

in: int

out: str

convert(1230213044) = convert(1, million) + convert(230, thousand) + convert(213) + convert(044)
one million two hundred thirty thousand two hundred thirteen fourtyfour

convert(213) = unique(2) hundred + unique(30) if unique(30) else second_digit_unique(3) + unique(0)


Special cases: 
	convert receiving less than 3 digits
	convert receiving three zeros 000, should not return anything
	remember that the second_digit unique must exist

"""
import enum
import unittest
from typing import List, Dict, Optional


unit_to_string: Dict[str, str] = {
"0": "","1": "One","2": "Two","3": "Three", "4": "Four","5": "Five","6": "Six","7": "Seven","8": "Eight","9": "Nine", "10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", "15": "Fifteen", "16":"Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen"
}

second_unit_to_string: Dict[str, str] = {
"0": "", "1": "", "2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty", "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety"
}


class NumberHouse(enum.Enum):
	hundred = 0
	thousand = 1
	million = 2
	billion = 3


PRINTABLE_HOUSES = [NumberHouse.thousand, NumberHouse.million, NumberHouse.billion]


def english_int(number: int) -> str:
	if number == 0:
		return 'Zero'

	result: List[str] = []
	
	house_count: int = 0
	while number > 0:
		remainder: int = number % 1000
		three_digit_remainder: str = turn_to_three_digit(str(remainder))
		result.append(convert(three_digit_remainder, NumberHouse(house_count)))
		number //= 1000
		house_count += 1

	# Reverse is needed cuz number is iterated backwards
	return ' '.join(reversed(result))


def turn_to_three_digit(number: str) -> str:
	while len(number) < 3:
		number = '0' + number
	return number


def convert(number: str, number_house: NumberHouse) -> str:
	""" Receives a three digit number and turns it into string representation"""
	if number == '000':
		return ''

	result: List[str] = []
	
	# converts the first number
	first_digit_text: Optional[str] = unit_to_string.get(number[0])
	if first_digit_text:
		result.append(first_digit_text + ' ' + NumberHouse.hundred.name)
	
	# Converts the last two digits
	have_unique_text_translation: bool = bool(unit_to_string.get(number[1:]))
	if have_unique_text_translation:
		result.append(unit_to_string[number[1:]])
	else:
		result.append(second_unit_to_string[number[1]] + ' ' + unit_to_string[number[2]])

	
	if number_house in PRINTABLE_HOUSES and result:
		result.append(number_house.name)
	return ' '.join(result)
	
	
class Test(unittest.TestCase):

	data = [
		(120, 'one hundred twenty'), 	
		(121, 'one hundred twenty one'), 	
		(1, 'one'), 	
		(1220, 'one thousand two hundred twenty'), 	
		(12202, 'twelve thousand two hundred two'), 	
		(120202, 'one hundred twenty thousand two hundred two'), 	
		(1120202, 'one million one hundred twenty thousand two hundred two'), 	
		(1000120202, 'one billion one hundred twenty thousand two hundred two'), 	
	]
	
	def test(self):
		for num, expected in self.data:
			self.assertEqual(english_int(num).lower().strip().replace('  ', ' '), expected.lower().strip())


if __name__ == '__main__':
	unittest.main()
