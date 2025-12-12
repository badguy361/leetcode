"""
695. Max Area of Island
"""
from typing import List
"""
作法:
DFS
時間複雜度: O(n)
空間複雜度: O(n)
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c) -> int:
            if r<0 or r>=rows or c<0 or c>=cols:
                return 0
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1
            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c-1)
            area += dfs(r,c+1)
            return area
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(dfs(i,j),max_area)
        return max_area
