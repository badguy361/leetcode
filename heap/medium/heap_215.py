"""
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""
# solution 1
"""
做法：
1. 使用堆排序，將數組中的元素存入堆中，並按降序排序
2. 遍歷堆，彈出前k-1個元素
3. 返回堆頂元素
"""
from typing import List
import heapq
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        for _ in range(k-1):
            heapq.heappop(max_heap)
        return -max_heap[0]

# solution 2
"""
做法：
1. 將數組中的元素按降序排序
2. 返回第k個元素
"""
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x:-x)
        return nums[k-1]
