"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""
# Test Case
nums = [1,2,3,4]

# solution 1
"""
做法:
1. 
複雜度:
- 時間複雜度: O(n)
- 空間複雜度: O(1)
"""
ans = [1]*len(nums)
left, right = 1,1
for i in range(len(nums)):
    ans[i] = left
    left *= nums[i]
for j in range(len(nums)-1,-1,-1):
    ans[j] = ans[j] * right
    right = right * nums[j]
print(ans)
