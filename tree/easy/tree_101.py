"""
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror 
of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""
# solution 1
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(n1,n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return n1.val == n2.val and isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)

        return isMirror(root.left, root.right)
