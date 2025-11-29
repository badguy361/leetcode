"""
239. Sliding Window Maximum
"""
from typing import List
from collections import deque

"""
做法: deque + monotonic queue
複雜度:
- 時間複雜度: O(n)
- 空間複雜度: O(n)
"""
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    ans = []
    dq = deque()
    for i, num in enumerate(nums):
        while dq and dq[0] <= i-k:
            dq.popleft()
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k-1:
            ans.append(nums[dq[0]])
    return ans
