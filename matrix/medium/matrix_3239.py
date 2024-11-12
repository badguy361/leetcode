"""
3293. Minimum Number of Flips to Make Binary Grid Palindromic I
You are given an m x n binary matrix grid.
A row or column is considered palindromic if its values read the same forward 
and backward.
You can flip any number of cells in grid from 0 to 1, or from 1 to 0.
Return the minimum number of cells that need to be flipped to make either 
all rows palindromic or all columns palindromic.

Example 1:
Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
Output: 2
Explanation:
Flipping the highlighted cells makes all the rows palindromic.

Example 2:
Input: grid = [[0,1],[1,1]]
Output: 1
Explanation:
Flipping the highlighted cell makes all the rows palindromic.

Example 3:
Input: grid = [[1],[0]]
Output: 0
Explanation:
All rows are already palindromic.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is either 0 or 1
"""
from typing import List
# solution 1
"""
做法: 原始做法
"""
# class Solution:
#     def minFlips(self, grid: List[List[int]]) -> int:
#         def check(row_or_column):
#             normal = row_or_column
#             reverse = row_or_column[::-1]
#             if normal == reverse:
#                 return True
#             else:
#                 return False

#         def flip(step, row_or_column):
#             a = 0
#             b = len(row_or_column)-1
#             while a < b:
#                 if row_or_column[a] == row_or_column[b]:
#                     a+=1
#                     b-=1
#                 else:
#                     row_or_column[b] = row_or_column[a]
#                     step += 1
#             return step

#         step = 0
#         step_row = 0
#         step_column = 0
#         column = [[ro[col] for ro in grid] for col in range(len(grid[0]))]
#         for ro in grid:
#             if not check(ro):
#                 step_row += flip(step, ro)
#         for col in column:
#             if not check(col):
#                 step_column += flip(step, col)

#         return min(step_row,step_column)

# solution 2
"""
做法: 優化做法
"""
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def check(row_or_column):
            return row_or_column == row_or_column[::-1]

        def flip(step, row_or_column):
            a, b = 0, len(row_or_column)-1
            while a < b:
                if row_or_column[a] != row_or_column[b]:
                    row_or_column[b] = row_or_column[a]
                    step += 1
                a+=1
                b-=1
            return step

        step = 0
        step_row = 0
        step_column = 0
        for row in grid:
            if not check(row):
                step_row += flip(step, row)

        for col in range(len(grid[0])):
            column = [row[col] for row in grid]
            if not check(column):
                step_column += flip(step, column)

        return min(step_row, step_column)
