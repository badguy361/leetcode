"""
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# solution 1:
"""
做法：
1. 交換當前節點和下一個節點的"值"
2. 返回修改後的linked list
時間複雜度：O(n)
"""
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         cur = head
#         while cur:
#             if cur.next:
#                 tmp = cur.next.val
#                 cur.next.val = cur.val
#                 cur.val = tmp
#                 cur = cur.next.next
#             else:
#                 break
#         return head

# solution 2:(符合題目要求)
"""
做法：
1. 使用一個dummy節點來處理邊界情況
2. 交換當前節點和下一個節點的"節點"
3. 返回修改後的linked list
時間複雜度：O(n)
"""
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next

            first.next = second.next

            cur.next = second
            cur.next.next = first
            cur = cur.next.next

        return dummy.next
