"""
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers be
numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same 
element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

"""

# Test Case
numbers = [2,7,11,15]
target = 9

# solution 1
"""
做法:
hashmap
時間複雜度: O(n)
空間複雜度: O(n)
"""
hashmap = {}

for i, num in enumerate(numbers):
    obj = target - num
    if obj in hashmap:
        print([hashmap[obj]+1, i+1])
    hashmap[num] = i

# solution2
"""
做法:
雙指針
時間複雜度: O(n)
空間複雜度: O(1)
"""
left = 0
right = len(numbers) - 1
while right > left:
    remain_sum = numbers[left] + numbers[right]
    if remain_sum < target:
        left += 1
    elif remain_sum > target:
        right -= 1
    else:
        print([left+1, right+1])
