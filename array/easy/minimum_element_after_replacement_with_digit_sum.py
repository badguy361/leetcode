"""
3300. Minimum Element After Replacement With Digit Sum:

You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.

 

Example 1:

Input: nums = [10,12,13,14]
Output: 1
Explanation: nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation: nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.

Example 3:

Input: nums = [999,19,199]
Output: 10
Explanation: nums becomes [27, 10, 19] after all replacements, with minimum element 10.


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 104

"""

# solution 1(faster):
"""
做法 : 轉string後遍歷相加
複雜度 : O(n*d) #d為每個數字string長度
"""
nums = [1, 2, 3, 5]
nums = list(map(str, nums))
new_nums = []
for i in nums:
    total = 0
    for j in i:
        total += int(j)
    new_nums.append(total)
ans = min(new_nums)
print(ans)

# solution 2:
"""
做法 : 用 // 與 % 做計算
複雜度 : O(n*d) #d為每個數字string長度
"""
nums = [1, 2, 3, 5]
min_num = 10
nums_new = []
for i in nums:
    total = 0
    tmp1 = i
    tmp2 = 0
    while tmp1 >= min_num:
        tmp2 = tmp1 % 10
        tmp1 = tmp1 // 10
        total += tmp2
    total += tmp1
    nums_new.append(total)
ans = min(nums_new)
print(ans)
