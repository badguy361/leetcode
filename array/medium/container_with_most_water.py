"""
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such 
that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container 
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this 
case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
# Test Case
height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]

# solution 1
"""
做法: 暴力解法
複雜度: O(n^2)
"""
# max_area = 0
# index1 = 0
# for hei in height:
#     index2 = index1 + 1
#     for hei2 in height[index2:]:
#         area = min(hei,hei2) * (index2 - index1)
#         max_area = max(max_area,area)
#         index2 += 1
#     index1 += 1
# print(max_area)

# solution 2
"""
做法: 雙指針
複雜度: O(n)
"""
max_area = 0
left = 0
right = len(height) - 1
for i in range(len(height)):
    if height[left] < height[right]:
        area = height[left] * (right - left)
        left += 1
    elif height[left] > height[right]:
        area = height[right] * (right - left)
        right -= 1
    else:
        area = min(height[left],height[right]) * (right - left)
        left += 1
        right -= 1
    max_area = max(max_area,area)
print(max_area)
