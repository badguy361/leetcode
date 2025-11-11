"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the
same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

# solution:
"""
做法: 遞迴
1. 如果兩個節點都為空，則返回True
2. 如果兩個節點只有一個為空，則返回False
3. 如果兩個節點的值不相等，則返回False
4. 遞迴比較兩個節點的左子樹和右子樹
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

p , q = [1,2,3] , [1,2,3]
# p , q = [1,2] , [1,None,2]
# p , q = [1,2,1] , [1,1,2]
root_p = TreeNode(1)
root_p.left = TreeNode(2)
root_p.right = TreeNode(3)

root_q = TreeNode(1)
root_q.left = TreeNode(2)
root_q.right = TreeNode(3)

solution = Solution()
output = solution.isSameTree(root_p,root_q)
print(output)
