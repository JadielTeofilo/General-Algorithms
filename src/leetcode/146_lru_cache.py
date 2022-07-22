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
    key: Optional[int] = None
    value: Optional[int] = None
    prev: Optional['ListNode'] = None
    next: Optional['ListNode'] = None


class Queue:

    def __init__(self) -> None:
        self.start: ListNode = ListNode()
        self.end: ListNode = ListNode()

        self.start.next = self.end
        self.end.prev = self.start

    def move_to_the_back(self, node: ListNode) -> None:
        self._remove_node(node)
        self._add_node(node)

    def append(self, key: int, value: int) -> ListNode:
        node: ListNode = ListNode(key, value)
        return self._add_node(node)

    def _add_node(self, node: ListNode) -> ListNode:
        node.next = self.start.next
        node.prev = self.start
        self.start.next.prev = node
        self.start.next = node
        return node

    def popleft(self) -> Optional[ListNode]:
        node: ListNode = self.end.prev
        self._remove_node(node)
        return node

    def _remove_node(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev


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
        self.capacity -= 1

    def evict(self) -> None:
        if self.capacity > 0:
            return
        self.capacity += 1
        node: Optional[ListNode] = self.queue.popleft()
        self.store.pop(node.key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

