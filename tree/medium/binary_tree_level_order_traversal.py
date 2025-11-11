"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its 
nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
#solution
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 1
        store = {}
        def Rec(root:Optional[TreeNode], level, store):
            if not root:
                return False
            store.setdefault(level, []).append(root.val)
            level += 1
            return Rec(root.left, level, store) or Rec(root.right, level, store)
        _ = Rec(root,level,store)

        if store:
            ans = [store[i] for i in store]
            return ans
        return []
        