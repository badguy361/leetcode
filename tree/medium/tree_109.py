"""
109. Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height 
balanced BST.

Input: head = []
Output: []

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# solution 1: 徒法煉鋼

from typing import Optional
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def headToList(head, head_list):
            if head is None:
                return head_list
            head_list.append(head.val)
            return headToList(head.next,head_list)

        def buildTree(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(head_list[mid])

            # Build left subtree
            node.left = buildTree(left, mid - 1)

            # Build right subtree
            node.right = buildTree(mid + 1, right)

            return node

        head_list = headToList(head, [])
        return buildTree(0, len(head_list) - 1)
