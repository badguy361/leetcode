"""
463. Island Perimeter
You are given row x col grid representing a map where grid[i][j] = 1 
represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one 
island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected
to the water around the island. One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine 
the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4
"""
# solution 1
"""
做法：分別計算row和col的周長，減去重複的邊
"""
from typing import List
# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         flag = 0
#         perimeter = 0
#         for row in grid:
#             for index, col in enumerate(row):
#                 if index < len(row)-1:
#                     if row[index] == 1 and row[index+1] == 1:
#                         flag -= 2
#                 if col == 1:
#                     perimeter += 4

#         for j in range(len(grid[0])):
#             col = [row[j] for row in grid]
#             for index in range(len(col)):
#                 if index < len(col)-1:
#                     if col[index] == 1 and col[index+1] == 1:
#                         flag -= 2

#         return perimeter + flag

# solution 2
"""
做法：一次計算row和col的周長，減去重複的邊
註：與數獨不同，數獨要把col抽離出來判斷，這裡可以直接看上一個col是否為1
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # Start with 4 sides for each land cell
                    perimeter += 4

                    # Check the cell above
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2

                    # Check the cell to the left
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2

        return perimeter
