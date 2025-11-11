"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily 
temperatures, return an array answer such that answer[i] is the 
number of days you have to wait after the i-th day to get a warmer 
temperature. If there is no future day for which this is possible, 
keep answer[i] == 0 instead.

Constraints:

1 <= temperatures.length <= 105
-231 <= temperatures[i] <= 231 - 1
"""

# solution 1
"""
做法:
使用monotonic stack
複雜度:
- 時間複雜度: O(2n)
- 空間複雜度: O(n)
"""
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
ans = len(temperatures) * [0]
stack = []
for i, temp in enumerate(temperatures):
    while stack and temp > temperatures[stack[-1]]:
        top_index = stack.pop()
        ans[top_index] = i - top_index
    stack.append(i)
print(ans)
