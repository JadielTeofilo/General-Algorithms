"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


we can either use 2 heaps or a SortedList

2 heaps:

    smaller: List[int]   # Max heap
    bigger: List[int]  # Min heap

insert
    if both empty, just insert on smaller and return
    else
        if num <= then smaller[0] add to it, else add to bigger
    balance the heaps
        if size differ by more then 1, we will move one element from the fullest to the other

pop
    if not one of them, return the single number
    if one of them is bigger, get from it and return 
    get from both and return avg


init
O(n) space

inserts
O(log n) time complexity
O(1) space complexity

pop
O(1) time complexity
O(1) space complexity





"""
import collections
import heapq


HeapValue = collections.namedtuple('HeapValue', 'index value')


class MedianFinder:

    def __init__(self):
        self.smaller: List[HeapValue] = []
        self.bigger: List[HeapValue] = []

    def addNum(self, num: int) -> None:
        if not self.smaller and not self.bigger:
            heapq.heappush(self.smaller, HeapValue(-num, num))
            return
        if num <= self.smaller[0].value:
            heapq.heappush(self.smaller, HeapValue(-num, num))
        else:
            heapq.heappush(self.bigger, HeapValue(num, num))
        self._balance_heaps()

    def findMedian(self) -> float:
        if not self.smaller or not self.bigger:
            return (self.smaller[0].value if self.smaller 
                    else self.bigger[0].value)
        if len(self.smaller) != len(self.bigger):
            return (self.smaller[0].value if len(self.smaller) > len(self.bigger)
                    else self.bigger[0].value)
        return (self.smaller[0].value + self.bigger[0].value) / 2

    def _balance_heaps(self) -> None:
        if abs(len(self.smaller) - len(self.bigger)) < 2:
            return
        if len(self.smaller) > len(self.bigger):
            origin: List[HeapValue] = self.smaller
            target: List[HeapValue] = self.bigger
        else:
            origin: List[HeapValue] = self.bigger
            target: List[HeapValue] = self.smaller
        popped_item: HeapValue = heapq.heappop(origin)
        heapq.heappush(
            target, 
            HeapValue(popped_item.index*-1, popped_item.value)
        )




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
