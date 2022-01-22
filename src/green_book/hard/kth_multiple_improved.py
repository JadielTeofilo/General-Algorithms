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



With the min heap you can get a time complexity of O(klog(k)) k=kth
We can do better though, we since the numbers are ordered if you separate them o 3x 5x and 7x
In stead of putting into que minheap, just use three queues, and put the new generated values there, 
split by the prime that generated it, to take the min, just popleft (use Set to duplicates)

"""
import heapq
from typing import List, Set


def kth_multiple(kth: int) -> int:
    if kth < 1:
        raise ValueError('Input must be at least 1')
    min_heap: List[int] = [1]
    visited: Set[int] = {1}
    number: int = 1
    while kth > 0:
        kth -= 1
        number = heapq.heappop(min_heap)
        add_new_values(min_heap, number, visited)
    return number


def add_new_values(min_heap: List[int], number: int, 
                   visited: Set[int]) -> None:
    primes: List[int] = [3, 5, 7]
    for prime in primes: 
        new_number: int = prime * number
        if new_number not in visited:
            visited.add(new_number)
            heapq.heappush(min_heap, new_number)


for i in range(1, 20):
    print(kth_multiple(i))
