"""
3217. Remove Nodes From Linked List
You are given an array of integers nums and the head of a linked 
list. Return the head of the modified linked list after removing 
all nodes from the linked list that have a value that exists in nums.

Example 1:
Input: nums = [1, 2, 3] head = [1, 2, 3, 4, 5]
Output: [4, 5]
Explanation: The nodes that should be removed are 1, 2 and 3.

Example 2:
Input: nums = [1], head = [1, 2, 1, 2, 1]
Output: [2, 2]
Explanation: The node with value 1 should be removed.

Example 3:
Input: nums = [5], head = [1, 2, 3, 4]
Output: [1, 2, 3, 4]
Explanation: No nodes should be removed.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 105
All elements in nums are unique.
The number of nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
The input is generated such that there is at least one node in the 
linked list that has a value not present in nums.
"""
# solution 1:
"""
做法：
1. 將nums轉為set
2. 遍歷linked list，如果遇到nums中的值，則將該node刪除
3. 返回修改後的linked list
時間複雜度：O(n)
"""
# NOTE: set的時間複雜度是O(1), List的時間複雜度是O(n)
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val in nums:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
