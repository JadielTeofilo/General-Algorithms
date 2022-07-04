"""
Implement a SnapshotArray that supports the following interface:

    SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
    void set(index, val) sets the element at the given index to be equal to val.
    int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
    int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id




1 2 3 4
2 2 3 4
2 2 1 3

matrix = [
[0] * size
]


when we get a snap we update our curr_index and append a new list with the same values as before


have a Dict[int, Dict[int | str, Any]]

[
{0: 1, 1: 2}
{},
{}
]



Set()
O(1) time
snap()
O(n) time
get()
O(1) time


"""
from typing import List, Any, Dict


Versions = List[Dict[int, int]]


class SnapshotArray:

    def __init__(self, length: int):
        self.versions: Versions = [dict()]
        self.curr_index = 0

    def set(self, index: int, val: int) -> None:
        self.versions[self.curr_index][index] = val

    def snap(self) -> int:
        self.curr_index += 1
        self.versions.append({})
        return self.curr_index - 1

    def get(self, index: int, snap_id: int) -> int:
        while snap_id >= 0:
            if self.versions[snap_id].get(index) is None:
                snap_id -= 1
                continue
            return self.versions[snap_id][index]
        return 0


