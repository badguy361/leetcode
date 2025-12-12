"""
997. Find the Town Judge
"""
# solution 1:
from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        indegree = [0]*(n+1)
        outdegree = [0]*(n+1)

        for i, j in trust:
            outdegree[i] += 1
            indegree[j] += 1

        for person in range(n+1):
            if indegree[person] == n-1 and outdegree[person] == 0:
                return person
        return -1
