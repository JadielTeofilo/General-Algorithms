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


OrderedDict = collections.OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.store: OrderedDict[int, int] = collections.OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self.store.move_to_end(key, last=True)
        return self.store[key]

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key] = value
            self.store.move_to_end(key)
            return
        self.evict()
        self.store[key] = value
    
    def evict(self) -> None:
        if len(self.store) < self.capacity:
            return
        self.store.popitem(last=False) 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
