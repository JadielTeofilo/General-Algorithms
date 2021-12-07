"""
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1


Your algorithm should run in O(n) time and use constant space.

Remove all elements <=0 ou > len
 3  4  N  1
 N  4 -3  1
-1  N -3 -4


replace the number with index = number-1 position and keep looping until finding a None or negative
Think duplicates
keep track of the spot where you stoped, after finding a stop point, start again from stop + 1
iterate on the array and find the first None
if no None found, return last + 1

O(n) time complexity where n is the size of the input array
O(1) space


"""
