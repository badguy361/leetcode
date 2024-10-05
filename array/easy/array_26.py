"""
26. Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""
# Test Case
nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]

# solution 1
"""
做法: 
1. 用dict記錄數字出現次數
2. 刪除重複
複雜度: O(n)
"""
# table = {}
# delete_index = []
# for index, i in enumerate(nums):
#     if i in table:
#         delete_index.append(index)
#     else:
#         table[i] = 1

# # 方法1：用reversed反轉刪除index，從後面開始刪除，避免刪除錯誤index
# for j in reversed(delete_index):
#     nums.pop(j)
# # 方法2：用list comprehension刪除
# # nums = [nums[j] for j in range(len(nums)) if j not in delete_index]
# print(nums)
# print(len(table))

# solution 2
"""
做法: 用set去除重複
複雜度: O(n)
"""
seen = set()
nums = [x for x in nums if not (x in seen or seen.add(x))]
print(nums)
