"""
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.



a triangle is valid if the sides a, b and c are so that:

a + b > c, b + c > a and a + c > b

if se sort it we know that a <= b <= c and so, a + c > b and b + c > a will always be true a (since c is bigger equal then both of them)





"""
