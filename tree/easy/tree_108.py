"""
Given an integer array nums where the elements are sorted in ascending 
order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of 
the two subtrees of every node never differs by more than one.
"""
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(nums: List[int]) -> Optional[TreeNode]:
            if len(nums) == 0:
                return None
            root_num = len(nums)//2
            print("root_num:", root_num)
            root = TreeNode(nums[root_num])
            print(root.val)
            print("---")
            root.left = rec(nums[:root_num])
            root.right = rec(nums[root_num+1:])
            return root
        return rec(nums)

nums = [-10,-3,0,5,9]
root = Solution().sortedArrayToBST(nums)
print(root.val)
