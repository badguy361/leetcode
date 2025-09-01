"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
# Test Case
nums = [100,4,200,1,3,2]

# solution 1
"""
做法:
複雜度:
- 時間複雜度: O(n)
- 空間複雜度: O(n)
"""
hashmap = set(nums)
max_length = 0
for num in nums:
    if num-1 not in hashmap:
        current_num = num
        current_length = 1
        while current_num+1 in hashmap:
            current_num += 1
            current_length += 1
        max_length = max(max_length,current_length)
print(max_length)
