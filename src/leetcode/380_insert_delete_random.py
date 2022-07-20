"""
Implement the RandomizedSet class:

    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.


sets are not indexable, so we can`t pick a random index and just use it

we could keep a list as well, but we would have to remove elements (O(n))

we could keep a list and never remove elements (mark as deleted). Maybe remove it from time to time
    on the get random, we try getting a random element, if we see a null we call the cleanup algo


we could go for a linked list

we could go for a bitarray

insert
O(1) time
remove
O(1) time
random
O(1) time amortized

A better approach is to swap the item to be removed with the last and just pop it
this is the way of removing a element on a list in O(1) time

"""
import random
from typing import Dict, List


class RandomizedSet:

    def __init__(self):
        self.randomized: Dict[int, int] = dict()
        self.index_values: List[int] = list()

    def insert(self, val: int) -> bool:
        if val in self.randomized:
            return False
        self.randomized[val] = len(self.index_values)
        self.index_values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomized:
            return False
        swapped: int = self.index_values[-1]
        self.index_values[self.randomized[val]], self.index_values[-1] = (
            self.index_values[-1], self.index_values[self.randomized[val]]
        )
        self.randomized[swapped] = self.randomized[val]
        self.randomized.pop(val)
        self.index_values.pop()
        return True

    def getRandom(self) -> int:
        index: int = random.randint(0, len(self.index_values) - 1)
        return self.index_values[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
