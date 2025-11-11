"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]
"""

# solution:
"""
做法: 中序遍歷(左中右)
1. 使用stack來儲存節點
2. 使用current來遍歷節點
3. 使用result來儲存結果
"""
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        current = root
        result = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result

# 建立二元樹節點
root = [1,2,3,4,5,None,8,None,None,6,7,9]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)


# 創建解法實例並調用中序遍歷方法
solution = Solution()
output = solution.inorderTraversal(root)
print(output)  # 輸出：[4, 2, 6, 5, 9, 7, 1, 3, 8]
