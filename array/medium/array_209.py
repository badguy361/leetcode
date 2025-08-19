"""
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal 
length of a subarray whose sum is greater than or equal to target. If there is no such subarray, 
return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

# Test Case
nums = [2,3,1,2,4,3]
target = 7

# solution 1
"""
做法:
遍歷所有可能的子陣列
複雜度: O(n^2)
"""
ans = float("inf")
for left in range(len(nums)):
    right = left + 1
    tempSum = nums[left]
    if tempSum >= target:
        ans = 1
        break
    while right < len(nums):
        tempSum = nums[right] + tempSum
        if tempSum >= target:
            ans = min(ans, right-left+1)
            print(" ans", left, right, ans)
            break
        if right == len(nums) - 1 and ans == float("inf"):
            ans = 0
        right += 1
print(ans)

# solution 2
"""
做法:
1. slide window
複雜度: O(n)
"""
left = 0
ans = float("inf")
tempSum = 0
for right in range(len(nums)):
    tempSum += nums[right]
    while tempSum >= target:
        ans = min(ans, right - left + 1)
        tempSum -= nums[left]
        left += 1
if ans == float("inf"):
    print(0)
else:
    print(ans)
