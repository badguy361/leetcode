"""
349. Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any
order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
# solution 1
"""
做法: 
1. 將 nums1 和 nums2 轉換成 set 以去除重複元素
2. 將 set 轉換成 list 並排序
3. 使用雙指針法找出兩個 list 的交集
"""
from typing import List

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         num1_set = set(nums1)
#         num2_set = set(nums2)
#         num_list1 = list(num1_set)
#         num_list2 = list(num2_set)
#         num_list1.sort()
#         num_list2.sort()
#         i = 0
#         j = 0
#         ans = []
#         while i < len(num_list1) and j < len(num_list2):
#             if num_list1[i] == num_list2[j]:
#                 ans.append(num_list1[i])
#                 i += 1
#                 j += 1
#             elif num_list1[i] > num_list2[j]:
#                 j += 1
#             elif num_list1[i] < num_list2[j]:
#                 i += 1

#         return ans

# solution 2
"""
做法: 
1. 將 nums1 和 nums2 轉換成 set 以去除重複元素
2. 使用 set 的交集找出兩個 list 的交集
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
