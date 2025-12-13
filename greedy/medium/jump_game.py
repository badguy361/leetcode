"""
55. Jump Game
"""
from typing import List
"""
作法:
Greedy
時間複雜度: O(n)
空間複雜度: O(1)
"""
class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0
        total = len(nums)
        for i in range(total):
            if i > farest:
                return False
            farest = max(farest, i+nums[i])
        return True

# solution 2:
"""
作法:
看成圖，做DFS，實際去跑每個node
時間複雜度: O(n^2)
空間複雜度: O(n)
"""
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def dfs(i):
            if i >= n - 1:
                return True

            max_jump = nums[i]
            for step in range(1, max_jump + 1):
                if dfs(i + step):
                    return True

            return False

        return dfs(0)
