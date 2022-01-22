"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""
import dataclasses
import collections
from typing import List, Optional


@dataclasses.dataclass
class Node:
    value: int
    next: Optional['Node'] = None

@dataclasses.dataclass
class LinkedList:
    
    def __init__(self) -> None:
        self.start: Optional[Node] = None
        self.end: Optional[Node] = None
        
    def insert(self, value: int) -> None:
        if not self.start:
            self.start = Node(value)
            self.end = self.start
        else:
            self.end.next = Node(value)
            self.end = self.end.next
            
    def __str__(self) -> str:
        return str(self.start)
    

@dataclasses.dataclass
class TreeNode:
    value: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None


TreeNodeMetadata = collections.namedtuple('TreeNodeMetadata', 'tree_node depth')


def turn_into_list_of_linked_lists(tree_root: TreeNode) -> List[LinkedList]:
    """ Does the BFS and appends to each linked list (one for each depth) """
    result: List[LinkedList] = []
    queue: collections.deque = collections.deque()
    queue.append(TreeNodeMetadata(tree_root, 0))
    while queue:
        node_metadata: Optional[TreeNodeMetadata] = queue.popleft()
        if not node_metadata.tree_node:
            continue
        if linked_list_is_empty(result, node_metadata.depth):
            result.append(LinkedList())
        result[node_metadata.depth].insert(node_metadata.tree_node.value)
        queue.append(TreeNodeMetadata(node_metadata.tree_node.left, node_metadata.depth + 1))
        queue.append(TreeNodeMetadata(node_metadata.tree_node.right, node_metadata.depth + 1))
        
    return result
    

def linked_list_is_empty(linked_lists: List[LinkedList], index) -> bool:
    """ Checks if there is a linked list in the correspondant index 
        of the list of linked lists """
    return len(linked_lists) <= index
    
asdf = TreeNode(value=5, left=TreeNode(value=2, left=TreeNode(value=1, left=None, right=None), right=TreeNode(value=3, left=None, right=TreeNode(value=4, left=None, right=None))), right=TreeNode(value=7, left=TreeNode(value=6, left=None, right=None), right=TreeNode(value=8, left=None, right=TreeNode(value=9, left=None, right=None))))
[print(a) for a in turn_into_list_of_linked_lists(asdf)]
