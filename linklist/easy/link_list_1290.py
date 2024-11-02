"""
1290. Convert Binary Number in a Linked List to Integer
Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Constraints:
The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""

# solution 1
"""
做法: 反轉鏈表，然後計算答案
時間複雜度: O(n)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        pre = None
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        head = pre

        flag = 0
        ans = 0
        while head:
            if head.val == 1:
                ans += 2**flag
            flag += 1
            head = head.next
        return ans

head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)

print(Solution().getDecimalValue(head))