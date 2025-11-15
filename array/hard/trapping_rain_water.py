"""
42. Trapping Rain Water
"""
from typing import List
# solution 1
"""
做法: 遍歷List
複雜度:
- 時間複雜度: O(n^2)
- 空間複雜度: O(1)
"""
def trap1(height: List[int]) -> int:
    ans = 0
    for i in range(len(height)):
        left_max = max(height[:i+1])
        right_max = max(height[i:])
        ans += min(left_max, right_max) - height[i]
    return ans

# solution 2
"""
做法: 雙指針
複雜度:
- 時間複雜度: O(n)
- 空間複雜度: O(1)
"""
def trap2(height: List[int]) -> int:
    l, r = 0, len(height)-1
    max_left, max_right, ans = 0, 0, 0
    while l < r:
        if height[l] < height[r]:
            if height[l] > max_left:
                max_left = height[l]
            else:
                ans += max_left - height[l]
            l += 1
        else:
            if height[r] > max_right:
                max_right = height[r]
            else:
                ans += max_right - height[r]
            r -= 1
    return ans
