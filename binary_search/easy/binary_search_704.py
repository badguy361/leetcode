"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:

1 <= nums.length <= 104
-104 < target <= 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""
# solution 1
"""
做法: binary search
複雜度:
- 時間複雜度: O(logn)
- 空間複雜度: O(1)
"""
nums = [-1,0,3,5,9,12]
target = 9
left, right = 0, len(nums) - 1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print(mid)
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(-1)
