"""

Given an array of real numbers greater than zero in form of strings.

Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 . 

Return 1 for true or 0 for false.


0.6 0.7 0.8 1.2 0.4
0.6 1.3 2.1 3.3 3.7 


brute force would be to just try all n^3 possibilities

the order does not matter
sorting is an option

Let us formally define our new ranges. Let A=(0,2/3), B=[2/3,1] and C=(1,2).
These new ranges leave us with ten unique combinations:

1.A, A, A
2.A, A, B
3.A, A, C
4.A, B, B
5.A, B, C
6.A, C, C
7.B, B, B
8.B, B, C
9.B, C, C
10.C, C, C

We can quickly deduce that cases 6, 7, 8, 9, and 10 are not possible (the total sum will always be greater than 2).

That leaves us with cases 1, 2, 3, 4, and 5.

We can check case 1 by looking at the three largest values in A. Say we have these highest values as : 0.500,0.6666,0.65777. This lies between 1 and 2. We only have to worry about underflow in this case, meaning the sum of highest values in this range may not be greater than 1. But we are sure that this will be less than 2. So we only have to check for the condition whether these are greater than 1 or not.

Now, what about case 2? Under case 2, we have two numbers in range A and one number in range B. We have to worry about underflow and overflow. To avoid underflow, let’s suppose that we select the two largest values in A. Let’s call the sum of those numbers s. The range of s will be (0,4/3). So we just need to determine if there is a value in B that is greater than 1−s and less than 2−s. Simple enough.

Under case 3, we have two numbers in range A and one number in range C. We just have to worry about overflow ( because to the presence of an integer from range C, we are sure that their sum will be greater than 1). To avoid overflow, let’s suppose that we select the two smallest values in A and the smallest value in C. If the sum of those numbers is in the range ((1,2), then this case has occurred.

Case 4 will be similar to case 2. Under case 4, we have one number in range A and two numbers in range B. We have to worry about overflow. To avoid overflow, let’s suppose that we select the two smallest values in BB. Let’s call the sum of those numbers s. The range of ss will be [4/3,2]. So we just need to determine if there is a value in A that is less than 2−s. Not bad.

Case 5 is pretty easy as well. We have to worry about overflow. To avoid overflow, let’s suppose that we select the smallest value in A, the smallest value in B, and the smallest value in C. If the sum of those numbers is in the range (1,2), then this case has occurred.


				




"""
