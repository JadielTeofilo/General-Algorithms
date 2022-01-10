"""
There is a row of seats. Assume that it contains N seats adjacent to each other. There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.

An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')

Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.

Return minimum value % MOD where MOD = 10000003

Example

Here is the row having 15 seats represented by the String (0, 1, 2, 3, ......... , 14) -

              . . . . x . . x x . . . x . .
              0 1 2 3 4 5 6 7 8 9 1011121314  

4, 7, 8, 12
4,5,8,12
6,7,8,12,13,141516

. . x x . x . . x
. . x x x . x .
. . . . . . . .

x x x . . . x . . . . x

when we see a gap, its better to go they're way if there are more elements to the right then to the left

find the places with xs 
4 7 8 12
0 1 2 3
3 2 1 0 (subtracting from the len(n) - 1)
keep a counter to get the hops
iterate on places, looking behind and update the two places and the counter


Now to make them sit together one of approaches is -
                  . . . . . . x x x x . . . . .

Following are the steps to achieve this -
1 - Move the person sitting at 4th index to 6th index -
    Number of jumps by him =   (6 - 4) = 2

2 - Bring the person sitting at 12th index to 9th index -
    Number of jumps by him = (12 - 9) = 3

So now the total number of jumps made =
    ( 2 + 3 ) % MOD =
    5 which is the minimum possible jumps to make them seat together.

There are also other ways to make them sit together but the number of jumps will exceed 5 and that will not be minimum.

For example bring them all towards the starting of the row i.e. start placing them from index 0.
In that case the total number of jumps will be
    ( 4 + 6 + 6 + 9 )%MOD
    = 25 which is very costly and not an optimized way to do this movement

In - spots: str
Out - int


"""
from typing import List


class Solution:
    # @param A : string
    # @return an integer
    def seats(self, spots: str) -> int:
        places: List[int] = [index 
                             for index, char in enumerate(spots) 
                             if char == 'x']
        counter: int = 0
        for index, seat in enumerate(places):
            if index == 0:
                continue
            counter += self.update_places(places, index)

        return counter

    def update_places(self, places: List[int], index: int) -> int:
        diff: int = places[index] - places[index - 1]
        if diff == 1:
            return 0
        prefix: int = index - 1  # Elements to the left of index - 1
        suffix: int = (len(places) - 1) - index  # Elements to the right of index
        if prefix > suffix:
            # Brings the right element to the left
            places[index] = places[index - 1] + 1 
            return diff - 1
        return diff * (prefix + 1)




        



