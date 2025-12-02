"""
226. Invert Binary Tree
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
做法: recursive
複雜度:
- 時間複雜度: O(n)
- 空間複雜度: O(h)
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tmp_l = root.left
        tmp_r = root.right
        root.left = tmp_r
        root.right = tmp_l
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
