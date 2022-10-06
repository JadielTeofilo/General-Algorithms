"""
 Circular Array: Implement a CircularArray class that supports an array-like data structure which
can be efficiently rotated. If possible, the class should use a generic type (also called a template), and should support iteration via the standard for (Obj 0 : circularArray) notation.

How is this going to be used

Should we assume that it will always fit in memory?

Where would you want to make insertions?

If we are not inserting in the middle of the list, we dont need a liked list

Does it have a fixed size


CircularArray
    start_node: Node
    

    __iter__()
    rotate()


Node
    value: Any
    next_node: 'Node'



1 -> 2 -> 3

Code bellow is wrongish

"""
import dataclasses
from typing import Iterator, Optional, Any
import unittest


@dataclasses.dataclass
class Node:
    value: Any
    next_node: Optional['Node'] = None


class CircularArray:

    def __init__(self):
        self.start_node: Optional[Node] = None

    def insert(self, value: Any) -> None:
        if self.start_node is None:
            self.start_node = Node(value)
            self.start_node.next_node = self.start_node
        else:
            aux: Optional[Node] = self.start_node.next_node
            self.start_node.next_node = Node(value)
            self.start_node.next_node.next_node = aux

    def rotate(self) -> None:
        self.start_node = self.start_node.next_node

    def __iter__(self) -> Iterator[Any]:
        aux: Node = self.start_node
        while True:
            yield aux.value
            aux = aux.next_node


class Test(unittest.TestCase):

    def test(self):
        array: CircularArray = CircularArray()
        array.insert(1)
        array.insert(2)
        array.insert(3)
        self.assertEquals(next(array.__iter__()), 1)
        array.rotate()
        iteration = array.__iter__()
        
        self.assertEquals(next(iteration), 3)
        self.assertEquals(next(iteration), 2)
        self.assertEquals(next(iteration), 1)


if __name__ == '__main__':
    unittest.main()
