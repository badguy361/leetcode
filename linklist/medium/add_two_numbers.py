"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# solution 1:
"""
做法：
1. 使用兩個指針分別遍歷l1和l2
2. 將兩個指針的值相加，並將結果存入ans中
3. 返回ans
時間複雜度：O(n)
"""
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         add = 0
#         ans = None
#         while (l1 is not None) or (l2 is not None):
#             if l1 is not None:
#                 l1_val = l1.val
#                 l1 = l1.next
#             else:
#                 l1_val = 0

#             if l2 is not None:
#                 l2_val = l2.val
#                 l2 = l2.next
#             else:
#                 l2_val = 0

#             sum_num = add + l1_val + l2_val
#             add = sum_num // 10 # 10位數
#             tmp = ListNode(sum_num % 10) # 個位數
#             if ans is None: # 第一個節點
#                 ans = tmp
#                 cur = ans
#             else:
#                 cur.next = tmp
#                 cur = cur.next
#         if add != 0: # 最後一個節點(若還有進位)
#             cur.next = ListNode(add)
#         return ans

# solution 2
"""
做法:
1. 使用dummy node來幫助我們建立新的linked list
2. 使用carry來存儲進位
3. 遍歷l1和l2，將每個節點的值相加，並將結果存入dummy node中
4. 返回dummy node的next
時間複雜度：O(n)
空間複雜度：O(1)
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            first = total % 10
            carry = total // 10
            curr.next = ListNode(first)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
