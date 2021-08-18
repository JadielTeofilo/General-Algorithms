################### Remove element from doubly linked list #####################
import dataclasses
from typing import Optional


@dataclasses.dataclass
class Node:
    value: int
    previous: Optional['Node'] = None
    next: Optional['Node'] = None


@dataclasses.dataclass
class Queue:
    start: Optional['Node']    = None
    end: Optional['Node'] = None

    def insert(self, value: int) -> None:
        if not self.start:
            self.start = Node(value)
            self.end = self.start
        else:
            self.end.next = Node(value, previous=self.end)
            self.end = self.end.next

    def popleft(self) -> int:
        if not self.start:
            raise ValueError('Popping from empty list')
        value: int = self.start.value
        if self.end == self.start:     # important 
            self.end = None
        self.start = self.start.next
        self.start.previous = None
        return value

    def remove(self, node: Node) -> None:
        previous: Optional['Node'] = node.previous
        next: Optional['Node'] = node.next
        # Updates neighbors
        if previous:
            previous.next = next
        if next:
            next.previous = previous

        # Updates object pointers if needed
        if self.start == node:
            self.start = self.start.next
        if self.end == node:
            self.end = self.end.previous


if __name__ == '__main__':
    test = Queue()
    test.insert(1)
    test.insert(2)
    test.insert(3)
    print(test)
    print(test.popleft())
    print(test)
    import pdb;pdb.set_trace()	
    test.remove(test.start)
    print(test)

