"""
133. Clone Graph
"""
from typing import Optional
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
作法:
DFS
時間複雜度: O(n)
空間複雜度: O(n)
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        new_graph = {}
        def dfs(n) -> Optional['Node']:
            if n in new_graph:
                return new_graph[n]
            copy = Node(n.val)
            new_graph[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)
