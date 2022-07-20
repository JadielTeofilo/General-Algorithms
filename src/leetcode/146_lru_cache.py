"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

use a queue to keep track of recently inserted items

[1 8 0 6]

use a dictionary to keep the key values and a pointer to the queue node



O(capacity) space complexity
O(1) get/put time complexity


get
    looks up on the key_value store and returns it
    updates queue usage

put 
    if present, update value and update queue usage
    check capacity, if full, remove one from queue
    if not present (look key_value) just add at the end of the queue


"""
import collections
import dataclasses
from typing import Dict, Optional


@dataclasses.dataclass
class ListNode:
    key: int
    value: int
    prev: Optional['ListNode'] = None
    next_: Optional['ListNode'] = None


class Queue:
    
    def __init__(self) -> None:
        self.start: Optional[ListNode] = None
        self.end: Optional[ListNode] = None

    def move_to_the_back(self, node: ListNode) -> None:
        if self.end == node:
            return
        if self.start == node:
            self.start = node.next_

        node.next_.prev = node.prev
        if node.prev:
            node.prev.next_ = node.next_
        node.next_ = None
        node.prev = self.end
        self.end.next_ = node

    def append(self, key: int, value: int) -> ListNode:
        new_node: ListNode = ListNode(key, value)
        if self.end:
            self.end.next_ = new_node
            new_node.prev = self.end
            self.end = self.end.next_
        else:
            self.end = new_node
        if not self.start:
            self.start = self.end
        return new_node

    def popleft(self) -> Optional[ListNode]:
        popped_node: Optional[ListNode] = self.start 
        if self.start == self.end:
            self.end = None
        self.start = self.start.next_
        return popped_node


Store = Dict[int, ListNode]


class LRUCache:

    def __init__(self, capacity: int):
        self.queue: Queue = Queue()
        self.store: Store = dict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self.queue.move_to_the_back(self.store[key])
        return self.store[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key].value = value
            self.queue.move_to_the_back(self.store[key])
            return
        self.evict()
        self.store[key] = self.queue.append(key, value)
    
    def evict(self) -> None:
        if len(self.store) < self.capacity:
            return
        node: Optional[ListNode] = self.queue.popleft()
        if node:
            self.store.pop(node.key)
               


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
