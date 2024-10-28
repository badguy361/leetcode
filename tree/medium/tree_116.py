"""
116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next 
right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should 
populate each next pointer to point to its next right node, just like in Figure B.
 The serialized output is in level order as connected by the next pointers, with 
 '#' signifying the end of each level.

Example 2:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000
"""
# solution 1
from typing import Optional
from collections import deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                next_node: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next_node = next_node

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None  # 應該返回 None 而不是空列表
        queue = deque([root])  # 使用 deque 作為佇列
        while queue:
            level_size = len(queue)  # 當前層的節點數
            for i in range(level_size):
                node = queue.popleft()
                # 設置 next 指針
                if i < level_size - 1:
                    node.next = queue[0]
                # 將左右子節點加入佇列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root  # 返回根節點
