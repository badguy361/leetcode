"""
207. Course Schedule
"""
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        state = [0] * numCourses

        def dfs(n:int) -> bool:
            if state[n] == 1:
                return False
            if state[n] == 2:
                return True

            state[n] = 1
            for nei in graph[n]:
                if not dfs(nei):
                    return False
            state[n] = 2
            return True

        for num in range(numCourses):
            if not dfs(num):
                return False
        return True
