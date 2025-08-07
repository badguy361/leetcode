"""
16. 3Sum Closest
Given an integer array nums, a target value target, and an integer k, return the k closest 
numbers to target in the array. The result should be sorted in ascending order.

You may return the answer in any order. The answer is guaranteed to be unique (except for the 
order that it is in).

 

Example 1:

Input: nums = [1,2,3], target = 2
Output: [2]
Explanation: The distance between 2 and 2 is 0, while the distance between 1 and 2 is 1, and the 
distance between 3 and 2 is 1. Therefore, the closest number to 2 is 2.
Example 2:

Input: nums = [1,2,3,4,5], target = 4
Output: [4]
"""

# Test Case
nums = [0,1,2]
target = 3

"""
做法:
1. 先排序
2. 用雙指針找target
時間複雜度: O(n^2)
空間複雜度: O(1)
"""
nums.sort()
ans = 9999999
for i, num in enumerate(nums):
    left = i + 1
    right = len(nums) - 1
    while right > left:
        value = num + nums[left] + nums[right] - target
        if abs(value) < abs(ans):
            ans = value
        if value < 0:
            left += 1
        elif value > 0:
            right -= 1
        else:
            print(target)
            break

print(ans+target)
