"""
Given a binary tree, return the preorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3

return [1,2,3].

Using recursion is not allowed.


while stack
    peek from the stack
    if not  visited 
        add to result
        add to visited
    if left and not in visited add to stack
    same for right
    else
        pop from stack - meaning there is no left or right left to be used

"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    def preorderTraversal(self, A):
        visited = set()
        stack = [A]
        result = []
        while stack:
            curr = stack[-1]
            if curr and curr.val not in visited:
                visited.add(curr.val)
                result.append(curr.val)
            if curr.left and curr.left.val not in visited:
                stack.append(curr.left)
            elif curr.right and curr.right.val not in visited:
                stack.append(curr.right)
            else:
                stack.pop()
        return result
