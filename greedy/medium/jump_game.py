"""
55. Jump Game
"""
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0
        total = len(nums)
        for i in range(total):
            if i > farest:
                return False
            farest = max(farest, i+nums[i])
        return True
