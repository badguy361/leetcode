"""
997. Find the Town Judge
"""
# solution 1:
"""
作法:
計算 indegree & outdegree list
時間複雜度: O(n)
空間複雜度: O(n)
"""
from typing import List
from collections import defaultdict
class Solution1:
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

# solution 2:
"""
作法:
使用Adjacency list
時間複雜度: O(n)
空間複雜度: O(n)
"""
class Solution2:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0]*(n+1)
        for a, b in trust:
            graph[a].append(b)
            indegree[b] += 1
        for person in range(1, n+1):
            if len(graph[person])==0 and indegree[person] == n-1:
                return person
        return -1
