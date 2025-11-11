"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers
 such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the 
same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""

# solution 1:
"""
做法 : 遍歷所有可能的組合
時間複雜度 : O(n^2)
空間複雜度 : O(1)
"""
nums = [4,3,3]
target = 6
ans = {}
index1 = 0
for i in nums:
    index2 = index1 + 1
    for j in nums[index1 + 1 :]:
        if i + j == target:
            ans = {index1, index2}
            print(list(ans))
        index2 += 1
    index1 += 1
print(ans)

# solution 2:
"""
做法 : 用 hashmap 紀錄每個數字的 index
時間複雜度 : O(n)
空間複雜度 : O(n) dict存了n個key-value pair
"""
nums = [4,3,3]
target = 6
pair = {}
for index, num in enumerate(nums):
    obj = target - num
    if obj in pair:
        print([pair[obj],index])
    pair[num] = index
