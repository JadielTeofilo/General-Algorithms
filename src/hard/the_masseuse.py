"""
The Masseuse: A popular masseuse receives a sequence of back-to-back appointment requests
and is debating which ones to accept. She needs a 15-minute break between appointments and
therefore she cannot accept any adjacent requests. Given a sequence of back-to-back appoint-
ment requests (all multiples of 15 minutes, none overlap, and none can be moved), find the optimal
(highest total booked minutes) set the masseuse can honor. Return the number of minutes.

O(n) time complexity
O(1) space complexity

In - appointments: List[int]
Out - int
"""
from typing import List


def the_masseuse(appointments: List[int]) -> int:
    if not appointments:
        raise ValueError('Empty list')
    if len(appointments) < 3:
        return max(appointments)
    last: int = appointments[-1]
    curr: int = max(last, appointments[-2])
    for i in range(len(appointments) - 3, -1, -1):
        appointment: int = appointments[i]
        aux_curr: int = curr
        curr = max(last + appointment, curr)
        last = aux_curr
    return curr

print(the_masseuse([30, 15, 60, 75, 45, 15, 15, 45]))
