"""
104. Maximum Depth of Binary Tree
"""
# solution 1
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         def findDepth(root: Optional[TreeNode], n):
#             if root is None:
#                 return 0
#             if root.left is None and root.right is None:
#                 return n
#             if root.left is None and root.right is not None:
#                 n+=1
#                 return findDepth(root.right,n)
#             if root.left is not None and root.right is None:
#                 n+=1
#                 return findDepth(root.left,n)
#             if root.left is not None and root.right is not None:
#                 n+=1
#                 return max(findDepth(root.left,n),findDepth(root.right,n))

#         return findDepth(root, 1)

"""
做法: recursive + DFS
複雜度:
- 時間複雜度: O(n)
- 空間複雜度: O(h)
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
