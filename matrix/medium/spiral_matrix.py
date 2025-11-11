"""
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
# solution 1
"""
做法: 上下左右四個邊界，從左到右，從上到下，從右到左，從下到上。
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 從左到右遍歷頂行
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # 從上到下遍歷右列
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # 從右到左遍歷底行
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # 從下到上遍歷左列
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
