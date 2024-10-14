"""
33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k 
(1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], 
nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated 
at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of 
target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

"""

# Test Case
# nums = [4,5,6,7,0,1,2]
# nums = [5,6,7,0,1,2,4]
# nums = [6,7,0,1,2,4,5]
nums = [3,1]
target = 1

# solution 1
"""
做法: 暴力解法
複雜度: O(n)
"""
# for index, num in enumerate(nums):
#     if num == target:
#         print(index)
#     elif index == len(nums) - 1 and num != target:
#         print(-1)

# solution 2
"""
做法: 二分搜尋法
複雜度: O(log n)
"""
low, height = 0, len(nums) - 1
while low <= height:
    mid = (low + height) // 2
    print("mid",mid)
    if nums[mid] == target:
        print('object',mid)
        break
    if nums[low] <= nums[mid]: # 判斷左半邊是否為遞增
        if nums[low] <= target <= nums[mid]: # 判斷target是否在左半邊
            height = mid - 1
        else:
            low = mid + 1
    elif nums[mid] <= nums[height]: # 判斷右半邊是否為遞增
        if nums[mid] <= target <= nums[height]: # 判斷target是否在右半邊
            low = mid + 1
        else:
            height = mid - 1
print(-1)
