"""
Operations: Write methods to implement the multiply, subtract, and divide operations for integers.
The results of all of these are integers. Use only the add operator.

Multiply:
In - left: int, right: int
Out - int

6 * 40 = mult(40, 3) + mult(40, 3)  # last one cached


Subtract: 
In - left: int, right:int
Out int

5 - 2 
I can add elements to 2 until its 5, that would be O(n) n being the diff between the nums
I can keep doubling elements until I pass 5 

can I take the twos complement of the number and add them?
Nope, that would require a subtraction


Divide
Int - left: int, right: int
Out - int

20/5 = 4 cuz 4*5 = 20

5 + 5 + 5





"""


def multiply(left: int, right: int) -> int:
	curr_sign: int = True if sign(left) ^ sign(right) else False 
	small: int = min(abs(left), abs(right))
	big: int = max(abs(left), abs(right))
	result: int = 0
	for _ in range(small):
		result += big
	return result if not curr_sign else -result


def sign(number: int) -> int:
	return (number >> 31) & 1


def subtraction(left: int, right: int) -> int:
	negative: bool = left < right
	small: int = min(left, right)
	big: int = max(left, right)
	result: int = 0
	jump: int = 1
	last: int = 0
	while small + result != big:
		if small + result > big:
			result = last
			jump = 1 
		last = result
		result += jump
		jump += jump
	return -result if negative else result


def division(left: int, right: int) -> int:
	negative: int = sign(left) ^ sign(right)
	num_iterator: int = 0
	num_jump: int = right
	result_jump: int = 1
	result: int = 0
	last_num: int = 0
	last_result: int = 0
	# We know that left is bigger than 
	# right since the result is geranteed to be int

	# Iterates finding how many of `right` takes to 
	# get `left`
	while num_iterator != left:
		if num_iterator > left:
			# Resets the values to a slow start
			num_iterator = last_num
			result = last_result
			num_jump = right
			result_jump = 1
			if num_iterator + num_jump > left:
				return result
		last_num = num_iterator
		num_iterator += num_jump
		num_jump += num_jump  # Doubles the jump to get O(log(n))
		last_result = result
		result += result_jump
		result_jump += result_jump
	return result if not negative else -result
	

print(multiply(3, 4))
print(multiply(3, 4))
print(division(2816, 321))
