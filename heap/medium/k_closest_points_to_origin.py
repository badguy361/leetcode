"""
973. K Closest Points to Origin
"""
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(ans, (-dist, point[0], point[1]))
            if len(ans) > k:
                heapq.heappop(ans)
        return [[x,y] for _,x,y in ans]
