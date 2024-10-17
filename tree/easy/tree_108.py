"""
Given an integer array nums where the elements are sorted in ascending 
order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of 
the two subtrees of every node never differs by more than one.
"""

# solution 1
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        print("total_nums:", nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node],
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :])
        )
# 示例输入
nums = [-10, -3, 0, 5, 9]
root = Solution().sortedArrayToBST(nums)
print(root.val)
print(root.left.val)
print(root.right.val)
