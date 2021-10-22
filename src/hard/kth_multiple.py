"""
Kth Multiple: Design an algorithm to find the kth number such that the only prime factors are 3,5,and 7. Note that 3,5, and 7 do not have to be factors, but it should not have any other prime factors.For example, the first several multiples would be (in order) 1,3,5,7,9,15,21.

brute force

go on each number and check what are its factors, stop on the kth


[3 5 7]


3^0 * 5^0 * 7^0 1
3^1 * 5^0 * 7^0 3
3^0 * 5^1 * 7^0 5
3^0 * 5^0 * 7^1 7
3^2 * 5^0 * 7^0 9
3^1 * 5^1 * 7^0 15
3^1 * 5^0 * 7^1 21
3^0 * 5^2 * 7^1 25


000
111





"""
from typing import List, Set


def kth_multiple(kth: int) -> int:
	target_primes: List[int] = [3, 5, 7]
	prime_index: int = 0
	generated_values: Set[int] = {1}
	number: int = 1 
	while kth > 1:
		print(f'a{target_primes[prime_index]}aaaa')
		for value in generated_values:
			test: int = value * target_primes[prime_index]
			if test not in generated_values:
				number = test
				break
		generated_values.add(number)
		prime_index = (prime_index + 1) % 3
		kth -= 1
	return number 

for i in range(1, 10):
	print(kth_multiple(i))	
