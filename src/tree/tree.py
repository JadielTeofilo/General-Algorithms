############ Binary Search Tree ############
import dataclasses
from typing import Optional


@dataclasses.dataclass
class TreeNode:
    left: Optional['TreeNode']
    right: Optional['TreeNode']
    value: int


class Tree:

    def __init__(self):
        self.root: TreeNode = None

    def insert(self, value: int) -> None:
        self.root = self.insert_helper(self.root, value)

    def insert_helper(self, node: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        if not node:
            return TreeNode(None, None, value)
        if value > node.value:
            node.right = self.insert_helper(node.right, value)
        else:
            node.left = self.insert_helper(node.left, value)
        return node
        
    def search(self, value: int) -> bool:
        return self.search_helper(self.root, value)

    def search_helper(self, node: TreeNode,  value: int) -> bool:
        if not node:
            return False
        if node.value == value:
            return True
        if value > node.value:
            return self.search_helper(node.right, value)
        else:
            return self.search_helper(node.left, value)

    def __str__(self) -> str:
        return str(self.root)

