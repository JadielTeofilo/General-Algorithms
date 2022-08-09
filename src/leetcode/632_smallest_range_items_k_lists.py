"""
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.


 1     5  8
   2 3
            9 10 11
 1 
            9      17


[  4,    10   ,15         ,24,26],
[0,    9   ,12      ,20],
[    5           ,18   ,22       ,30]


itearate on the input keeping track of the visited lists then when we reach all lists 

have a heap pointing to all smallerst elements
pop from the heap, add to queue and add the new element from that list to the heap
add to counter
when counter is the size of k, we update the result and popleft from queue, and update counter


start = min(num[0] for num in nums)  # 1
end = max(num[-1] for num in nums)  # 17

O(nlogk) time where n is the sum of elements on all the lists and k is the num of lists
O(k) space for the heap and queue

"""
import collections
import heapq
from typing import List, Dict, Deque


NumMeta = collections.namedtuple('NumMeta', 'num num_index index')


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Builds the heap with the smallest elements
        heap: List[NumMeta] = [NumMeta(num[0], 0, i)
                               for i, num in enumerate(nums)]
        heapq.heapify(heap)
        counter: Dict[int, int] = collections.defaultdict(int)
        queue: Deque[NumMeta] = collections.deque()
        result: List[int] = [0, sys.maxsize]
        while heap:
            num, num_index, index = heapq.heappop(heap)
            if num_index + 1 < len(nums[index]):
                heapq.heappush(heap, NumMeta(nums[index][num_index + 1], num_index + 1, index))
            queue.append(NumMeta(num, num_index, index))
            counter[index] += 1
            while len(counter) >= len(nums):
                result = update_result(result, queue, nums)
                _, _, index = queue.popleft()
                counter[index] -= 1
                if counter[index] == 0:
                    counter.pop(index)
        return result


def update_result(result: List[int], queue: Deque[NumMeta],
                  nums: List[int]) -> List[int]:
    new_result: List[int] = [nums[queue[0].index][queue[0].num_index], nums[queue[-1].index][queue[-1].num_index]]
    new_diff: int = new_result[-1] - new_result[0]
    old_diff: int = result[-1] - result[0]
    if new_diff < old_diff:
        return new_result
    return result


