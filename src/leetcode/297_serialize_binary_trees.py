"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

preorder traversal (marking null nodes)


                    1
        5                       9
    2                   6
                    8

1 5 2 n n n 9 6 8 n n n n


                    1
        5                       9
    2                       6
                        8


"""
from typing import List, Dict, Optional, Iterator


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        string_builder: List[str] = list(preorder(root))
        return '|'.join(string_builder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes: List[str] = data.split('|')
        start: Dict[str, int] = dict(value=0)
        return self._build_tree_helper(nodes, start)

    def _build_tree_helper(self, nodes: List[str], 
                           start: Dict[str, int]) -> Optional[TreeNode]:
        if start['value'] >= len(nodes):
            return None
        curr: str = nodes[start['value']]
        start['value'] += 1
        if curr == 'n':
            return None
        curr_node: TreeNode = TreeNode(int(curr))
        curr_node.left = self._build_tree_helper(nodes, start)
        curr_node.right = self._build_tree_helper(nodes, start)
        return curr_node


def preorder(node: Optional[TreeNode]) -> Iterator[str]:
    if not node:
        yield 'n'
        return
    yield str(node.val)
    yield from preorder(node.left)
    yield from preorder(node.right)


