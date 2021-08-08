############ Linked List Queue ############
from typing import Any, Optional, List
import dataclasses


@dataclasses.dataclass
class Node:
    value: Any
    next: Optional['Node'] = None


class Queue:
    """ Implements a queue using a linked list """

    def __init__(self) -> None:
        self.last_element: Optional[Node] = None
        self.first_element: Optional[Node] = None
        
    def append(self, value: Any) -> None:
        new_node = Node(value=value)        
        if not self.last_element:
            self.last_element = new_node
            self.first_element = new_node
        else:
            self.last_element.next = new_node
            self.last_element = new_node

    def pop(self) -> Any:
        if not self.first_element:
            raise IndexError('pop from empty queue')
        second_element: Optional[Node] = self.first_element.next
        popped: Any = self.first_element.value
        # Case with single element on the list
        if self.last_element == self.first_element:
            self.last_element = None
        self.first_element = second_element
        return popped

    def __bool__(self) -> bool:
        return bool(self.last_element)

    def __str__(self) -> str:
        return str(self.first_element)


if __name__ == '__main__':
    q = Queue()
    items: List[Any] = [1, 'asdf', 1.2]
    [q.append(a) for a in items]
    print(q)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    if not q:
        print('empty')
    import pdb;pdb.set_trace()
    
    

