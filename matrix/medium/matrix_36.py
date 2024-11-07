"""
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according 
to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.

"""
# solution 1
"""
做法：超慢解法
"""
from typing import List
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         def trans(row_or_column):
#             flag = 0
#             for i, rc in enumerate(row_or_column):
#                 if rc == ".":
#                     row_or_column[i] = "." + str(flag)
#                     flag += 1
#                 else:
#                     try:
#                         row_or_column[i] = int(row_or_column[i])
#                     except ValueError:
#                         pass
#             return row_or_column

#         for i in range(9):
#             row = trans(board[i][:])
#             if len(set(row))!=9:
#                 return False

#         for j in range(9):
#             column = [row[j] for row in board]
#             column = trans(column)
#             if len(set(column))!=9:
#                 return False

#         k = 0
#         while k < 9:
#             n = 0
#             while n<9:
#                 check = {"1":False,"2":False,"3":False,"4":False,"5":False,"6":False,"7":False,
#                        "8":False,"9":False}
#                 for m in range(3):
#                     if board[k][m+n].isdigit():
#                         if not check[str(board[k][m+n])]:
#                             check[str(board[k][m+n])] = True
#                         elif check[str(board[k][m+n])]:
#                             return False
#                     if board[k+1][m+n].isdigit():
#                         if not check[str(board[k+1][m+n])]:
#                             check[str(board[k+1][m+n])] = True
#                         elif check[str(board[k+1][m+n])]:
#                             return False
#                     if board[k+2][m+n].isdigit():
#                         if not check[str(board[k+2][m+n])]:
#                             check[str(board[k+2][m+n])] = True
#                         elif check[str(board[k+2][m+n])]:
#                             return False
#                 n+=3
#             k += 3
#         return True

# solution 2
"""
做法：優化解法，抽象相同邏輯，hash table
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_repeat(data):
            check = set()
            for da in data:
                if da.isdigit():
                    if da in check:
                        return False
                    check.add(da)
            return True

        row = [i for i in board]
        for ro in row:
            response_row = check_repeat(ro)
            if not response_row:
                return False

        for j in range(9):
            col = [i[j] for i in board]
            response_col = check_repeat(col)
            if not response_col:
                return False

        for k in range(0,9,3):
            for m in range(0,9,3):
                box = [board[ro][co] for ro in range(k,k+3) for co in range(m,m+3)]
                response_box = check_repeat(box)
                if not response_box:
                    return False

        return True
