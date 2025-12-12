"""
200. Number of Islands
"""
from typing import List
"""
作法:
DFS
時間複雜度: O(n)
空間複雜度: O(n)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ans+=1
        return ans
