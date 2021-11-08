"""
Count of 2s: Write a method to count the number of 2s between 0 and n.


The catch is to make it unit by unit.

In - number: int
Out - int


6421




"""


def counts_of_two(number: int) -> int:
	""" Finds the count of all digits two 
		from 0 to number """
	result: int = 0
	for unit in range(digits_count(number)):
		result += count_twos_occurrences(unit, number) 
	return result


def count_twos_occurrences(unit: int, number: int) -> int:
	digit: int = get_digit(unit, number)  
	rounded_down_number: int = empty_units(number, from_unit=unit)   
	rounded_up_number: int = rounded_down_number + 10 ** (unit + 1)
	if digit < 2:
		return rounded_down_number // 10
	elif digit == 2:
		twos_from_right: int = (number % (unit * 10)) if unit > 0 else 0
		return rounded_down_number // 10 + twos_from_right + 1
	else:
		return rounded_up_number // 10  # 2 + 1


def empty_units(number: int, from_unit: int) -> int:
	"""
	Puts zeros on all digits from the from_unit
	num being 152 and from_unit being 1 gives 100

	"""
	mask: int = int(10 ** (from_unit + 1))
	return number - (number % mask)


def get_digit(unit: int, number: int) -> int:
	"""
		Finds the digit on the given unit
	"""
	# Gets the number to have the desired 
	# digit on the last unit
	while unit > 0:
		number //= 10
		unit -= 1

	return number % 10


def digits_count(number: int) -> int:
	count: int = 0
	while number > 0:
		number //= 10
		count += 1
	return count


print(counts_of_two(1321))
import pdb;pdb.set_trace()
