""" 
36. Valid Sudoku
"""
from typing import List

"""
solution 1: 
作法: 使用 set 
複雜度: O(n^2)
空間複雜度: O(n)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue

                index = (i//3) * 3 + (j//3)
                if (
                    value in columns[j] or
                    value in rows[i] or
                    value in boxes[index]
                ):
                    return False
                rows[i].add(value)
                columns[j].add(value)
                boxes[index].add(value)
        return True
