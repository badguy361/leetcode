"""
543. Diameter of Binary Tree
"""
# solution 1
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(left+right, self.ans)
            return max(left,right) + 1
        depth(root)
        return self.ans
