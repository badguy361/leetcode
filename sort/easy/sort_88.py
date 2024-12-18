"""
88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing 
order, and two integers m and n, representing the number of elements in 
nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead 
be stored inside the array nums1. To accommodate this, nums1 has a length of 
m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there 
to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""
# solution 1
"""
做法: 
1. 使用雙指針，從後往前遍歷
2. 比較nums1和nums2的大小，將大的數字放到nums1的後面
3. 如果nums1已經遍歷完，則將nums2剩下的數字依次放入nums1
複雜度: O(m+n)
"""
from typing import List
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         i,j = 0,0
#         sort = []
#         nums1[:] = nums1[:m]
#         while i < m and j < n:
#             if nums1[i] < nums2[j]:
#                 sort.append(nums1[i])
#                 i += 1
#             elif nums1[i] >= nums2[j]:
#                 sort.append(nums2[j])
#                 j += 1

#         sort.extend(nums1[i:])
#         sort.extend(nums2[j:])

#         nums1[:] = sort

# solution 2
"""
做法: 
1. 從後往前遍歷，比較nums1和nums2的大小，將大的數字放到nums1的後面
2. 如果nums1已經遍歷完，則將nums2剩下的數字依次放入nums1
複雜度: O(m+n)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of nums1 and nums2
        last = m + n - 1
        i, j = m - 1, n - 1

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1

        # If there are remaining elements in nums2, copy them
        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1
