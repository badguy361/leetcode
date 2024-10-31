"""
206. reverse linked list
Given the head of a singly linked list, reverse the list, and return 
the reversed list.

Example1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example2:
Input: head = [1,2]
Output: [2,1]

Example3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up:
A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

# solution 1:
"""
做法：將stack反序後，重新建立linked list
時間複雜度：O(n)
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = head
        stack = []
        while index:
            if index.next:
                stack.append(index.val)
            index = index.next

        head = None

        for sta in stack[::-1]:
            if not head:
                head = ListNode(sta)
                current = head
            else:
                current.next = ListNode(sta)
                current = current.next

        return head

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = Solution().reverseList(head)
print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)
