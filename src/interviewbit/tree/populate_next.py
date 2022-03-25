"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

    Note:

        You may only use constant extra space.

Example :

Given the following binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5- >6->  7 -> NULL
1   3 8 2 4 4 1 1

    Note 1:  that using recursion has memory overhead and does not qualify for constant space.

    Note 2: The tree need not be a perfect binary tree.


It is possible to traverse bfs in a reverse manner (just put right first)

It is possible to traverse **perfect trees** with bfs in O(1) if you have a next pointer 
    Just iterate while curr, then make curr = root.left, root = root.left


iterate while we have a curr

the left -> next receives right
right -> next receives root -> next -> left if curr -> next else None

curr = curr -> next

then make the curr = root.left, root = root.left changing the level

O(n) time
O(1) space


"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root: TreeNode) -> TreeNode:
        head: TreeNode = root
        curr: TreeNode = root
        while root:
            while curr:
                if curr.left:
                    curr.left.next = curr.right
                if curr.right:
                    curr.right.next = curr.next.left if curr.next else None
                curr = curr.next
            curr = root.left
            root = root.left
        return head

        

