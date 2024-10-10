"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""
# Test Case
nums = [1,3,5,6]
# target = 5
target = 2
# target = 7
# target = 0

# solution
"""
做法:
1. 使用二分搜尋法
2. 如果找到目標值，回傳目標值的索引
3. 如果找不到目標值，回傳插入位置的索引
複雜度: O(log n)
"""
low, height = 0 , len(nums) - 1
flag = ""
while low <= height:
    mid = (low + height) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] <= target:
        flag = "low"
        low = mid + 1
    elif nums[mid] >= target:
        flag = "height"
        height = mid - 1
if flag == "low":
    print("low")
    print(mid+1)
elif flag == "height":
    print("height")
    print(mid)

