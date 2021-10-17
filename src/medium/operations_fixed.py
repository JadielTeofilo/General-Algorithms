"""
Operations: Write methods to implement the multiply, subtract, and divide operations for integers.
The results of all of these are integers. Use only the add operator.

"""


def negate(number: int) -> int:
	if number == 0: 
		return number
	num_was_negative: bool = number < 0
	start: int = 1 if num_was_negative else -1
	iterator: int = 0
	jump: int = start
	while number != 0:
		if ((num_was_negative and number + jump > 0) or 
			(not num_was_negative and number + jump < 0)):
			jump = start
		last = iterator
		iterator += jump
		number += jump
		jump += jump
	return iterator


def subtraction(left: int, right: int) -> int:
	return left + negate(right)


def multiplication(left: int, right: int) -> int:
	if left < right:
		return multiplication(right, left)	

	# Signs are different
	is_negative: bool = bool(sign(left) ^ sign(right))
	
	number_iterator: int = 0

	for _ in range(abs(left)):
		number_iterator += abs(right)

	return number_iterator if not is_negative else negate(number_iterator)


def sign(number: int) -> int:
	return (number >> 31) & 1


def division(left: int, right: int) -> int:
	if right == 0:
		raise ZeroDivisionError
	if left < right:
		return 0
	# Case signs are different
	is_negative: bool = bool(sign(left) ^ sign(right))
	left = abs(left)
	right = abs(right)
	number_iterator: int = right
	jump: int = right
	result: int = 1
	result_jump: int = 1
	while number_iterator != left:
		# Resets if went too far
		if number_iterator + jump > left:
			if jump == right or number_iterator + right > left:
				break
			# Resets jump
			jump = right
			result_jump = 1
		result += result_jump
		result_jump += result_jump
		number_iterator += jump
		jump += jump  # Doubles jump every time

	return result if not is_negative else negate(result)




print(division(123, 32), multiplication(32, 3), subtraction(2,3))
