"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".



Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"


{
key: {timestamp: value},
1: {foo: bar}

}

Dict[str, SortedDict[str, int]]

we look the key in the dict
if not found, return ''
if found, bisect_left to find the desired timestamp

if you have only one item

2 4 6 

you could be exactly it, bigger then it or smaller




"""
import collections
import sortedcontainers
from typing import Dict


Store = Dict[str, sortedcontainers.SortedDict]


class TimeMap:

    def __init__(self):
        self.store: Store = collections.defaultdict(
            sortedcontainers.SortedDict
        )

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        curr: sortedcontainers.SortedDict = self.store[key]
        closest_timestamp: int = curr.bisect_right(timestamp) - 1
        if closest_timestamp < 0:
            return ''
        return curr.peekitem(closest_timestamp)[1]


