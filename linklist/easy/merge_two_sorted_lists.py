"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# solution 1
"""
做法: linked list
複雜度:
- 時間複雜度: O(n+m)
- 空間複雜度: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

curr1 = list1
curr2 = list2
dummy = ListNode()
tail = dummy

while curr1 and curr2:
    if curr1.val > curr2.val:
        tail.next = curr2
        curr2 = curr2.next
    else:
        tail.next = curr1
        curr1 = curr1.next
    tail = tail.next
if curr1 is not None:
    tail.next = curr1
if curr2 is not None:
    tail.next = curr2
print(dummy.next)
