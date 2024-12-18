"""
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
# solution 1
"""
做法：
1. 使用堆排序，將頻率存入堆中，並按頻率降序排序
2. 遍歷堆，彈出前k個元素
3. 返回堆頂元素
"""
from typing import List
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap=[(-freq,num) for num,freq in Counter(nums).items()]
        heapq.heapify(max_heap)
        ans_list = []
        for _ in range(k):
            _, ans = heapq.heappop(max_heap)
            ans_list.append(ans)
        return ans_list
