"""
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where
ach integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using
only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 
Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one
integer which appears two or more times.
"""

# solution 1
"""
做法: 快慢指針找環節點
複雜度: O(n)
空間複雜度: O(1)
"""
nums = [1,3,4,2,2]
slow = nums[0]
fast = nums[0]
while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break
slow = nums[0]
while slow != fast:
    slow = nums[slow]
    fast = nums[fast]
print(slow)
