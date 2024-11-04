"""
3142. Check if Grid Satisfies Conditions

You are given a 2D integer array grid of size n x n. You are also given an integer k.
The grid is said to satisfy the conditions if for every row and column, the difference 
between the maximum and minimum element is at most k.
Return true if the grid satisfies the conditions, otherwise return false.

Example 1:
Input: grid = [[1,0,2],[1,0,2]]
Output: true
Explanation: All the cells in the grid satisfy the conditions.

Example 2:
Input: grid = [[1,1,1],[0,0,0]]
Output: false
Explanation: All cells in the first row are equal.

Example 3:
Input: grid = [[1],[2],[3]]
Output: false
Explanation: All cells in the first row are equal.

Constraints:
1 <= n, m <= 10
0 <= grid[i][j] <= 9
"""
# solution 1:
"""
做法：
遍歷每一行，檢查每行中的最大值和最小值之差是否小於等於k
遍歷每一列，檢查每列中的最大值和最小值之差是否小於等於k
如果所有行和列都滿足條件，則返回true，否則返回false
複雜度：
時間複雜度：O(n^2)
空間複雜度：O(1)
"""
from typing import List
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i, in range(len(grid)): # Different from the cell to its right
            for j in range(len(grid[0])):
                if j < len(grid[0]) - 1:
                    if grid[i][j] == grid[i][j+1]:
                        return False

        for k in range(len(grid[0])): # Equal to the cell below it
            for m in range(len(grid)):
                if m < len(grid) - 1:
                    if grid[m][k] != grid[m+1][k]:
                        return False

        return True
