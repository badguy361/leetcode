"""
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""

# solution 1
"""
做法:
使用 binary search
複雜度:
- 時間複雜度: O(log(m * n))
- 空間複雜度: O(1)
"""
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
left = 0
right = len(matrix) - 1
while left <= right:
    mid = (right + left + 1) // 2
    if matrix[mid][0] <= target <= matrix[mid][-1]:
        for mat in matrix[mid]:
            if mat == target:
                print(True)
        print(False)
    if matrix[mid][0] > target:
        right = mid - 1
    if matrix[mid][-1] < target:
        left = mid + 1
print(False)
