"""
Number Max: Write a method that finds the maximum of two numbers. You should not use if-else
or any other comparison operator.


In - left: int, right: int
Out - max: int

integers?
yup


left += right

5 6
_ _ _ _ _ | _ _ _ _ _ _

101
110

5 - 6 = -1 get the 31th bit = 1
6 - 5 = 1 get the 31th bit = 0
6 + 5 = 11

0 * 5 + 1 * 6 = 6

-1 and -4

-1 + 4 = sign_0
-4 + 1 = sign_1
Problem when a is INT_MAX and b is negative:
INT_MAX - (-2)
will overflow and make the sign of this be negative (wont happen in python)

"""


def number_max(left: int, right: int) -> int:

	# If the sign is diff we just take the one that is positive
	sign_diff: int = sign(left) ^ sign(right)

	left_rest: int = left - right
	right_rest: int = right - left
	
	regular_result: int = (sign(left_rest) * right + 
						   sign(right_rest) * left)
	diff_sign_result: int = (sign(left) * right 
							 + sign(right) * left) 
	
	return (sign_diff * diff_sign_result + 
		    (sign_diff ^ 1) * regular_result)


def sign(number: int) -> int:
	return (number >> 31) & 1
	

print(number_max(3, 4), 4)
print(number_max(32, 4), 32)
print(number_max(123, 43), 123)
print(number_max(-1, -4), -1)
print(number_max(33, -44), 33)
