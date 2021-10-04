"""
Factorial Zeros: Write an algorithm which computes the number of trailing zeros in n factorial.

By that you mean the number of digits?
No, the zeros them selves

5! = 5*4*3*2*1 = 120 = 1 zero
1 = 1
1 2 = 2
1 2 3 = 6
1 2 3 4 = 24
1 2 3 4 5 = 120
1 2 3 4 5 6 = 720
1 2 3 4 5 6 7 = 5040
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
The numbers that generate a zero are:
_ 2 _ _ 5 _ _ _ _ 10  _  _  _ 14 15
the five multiplied by an even number and the ten it self 

25 accounts for two fives


If you multiply an even number by five it will have a zero at the end

So you can iterate on the values from 2 to n and counting the factors of 5

O(N) time complexity where N is the inputed number


In - number: int
Out - int



"""


def factorial_zeros(number: int) -> int:
	if number < 5:
		return 0
	count: int = 0
	for num in range(1, number + 1):
		while num % 5 == 0:
			num //= 5
			count += 1
	return count


print(factorial_zeros(3))
print(factorial_zeros(5))
print(factorial_zeros(10))
print(factorial_zeros(17))
print(factorial_zeros(27))
print(factorial_zeros(37))
