"""
143. Reorder List
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 10^4].
1 <= Node.val <= 1000
"""

# solution 1
"""
做法: linked list
複雜度:
- 時間複雜度: O(n)
- 空間複雜度: O(1)
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

def reorderList(head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return

    # Step 1: find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse second half
    prev, curr = None, slow.next
    slow.next = None  # cut the list
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    # Step 3: merge two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
