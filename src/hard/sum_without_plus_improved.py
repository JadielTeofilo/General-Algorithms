"""
Add Without Plus: Write a function that adds two numbers. You should not use + or any arithmetic
operators.



"""


def sum_(first: int, second: int) -> int:
    if second == 0:
        return first
    result: int = first ^ second
    carry: int = (first & second) << 1
    return sum_(result, carry)


print(sum_(2,5))
print(sum_(22,51))
print(sum_(211,5))
print(sum_(2,-23))
