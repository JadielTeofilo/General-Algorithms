############ Tree Traversal ############
from typing import Iterator

import tree


def inorder(node: tree.TreeNode) -> None:
    """ Prints values from tree with in order traversal"""
    if not node:
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)


def postorder(node: tree.TreeNode) -> None:
    """ Prints values from tree with post order traversal"""
    if not node:
        return
    inorder(node.left)
    inorder(node.right)
    print(node.value)


def preorder(node: tree.TreeNode) -> None:
    """ Prints values from tree with pre order traversal"""
    if not node:
        return
    print(node.value)
    inorder(node.left)
    inorder(node.right)


def inorder_yilder(node: tree.TreeNode) -> Iterator[int]:
    """ Prints values from tree with in order traversal"""
    if not node:
        return
    yield from inorder_yilder(node.left)
    yield node.value
    yield from inorder_yilder(node.right)


import pdb;pdb.set_trace()
