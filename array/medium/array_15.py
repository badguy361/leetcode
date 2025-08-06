"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
# Test Case
# nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
# nums = [0,0,0]
nums = [3,0,-2,-1,1,2]
# nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

# solution 1
"""
做法:
1. 先排序
2. 遍歷找target
3. 用set去重
複雜度: O(n^3)
"""
nums.sort()
# ans =  set()
# for i in range(len(nums)-1):
#     k = len(nums)-1
#     while k > i:
#         target = -(nums[i] + nums[k])
#         if target in nums[i+1:k]:
#             ans.add(tuple(sorted([nums[i], nums[k], target])))
#         k -= 1

# solution 2
"""
做法:
1. 先排序
2. 用雙指針找target
3. 用set去重
複雜度: O(n^2)
"""
ans=[]
for i,num in enumerate(nums):
    if i > 0 and num == nums[i - 1]:
        continue
    left = i+1
    right = len(nums)-1
    while right > left:
        total = num+nums[left]+nums[right]
        if total>0:
            right-=1
        elif total<0:
            left+=1
        else:
            ans.append([num,nums[left],nums[right]])
            while right>left and nums[right]==nums[right-1]:
                right-=1
            while right>left and nums[left]==nums[left+1]:
                left+=1
            right-=1
            left+=1

print(ans)
