"""
134. Gas Station
"""
from typing import List
"""
作法:
Greedy
時間複雜度: O(n)
空間複雜度: O(1)
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = 0
        tank = 0
        for i in range(len(gas)):
            total = total + gas[i] - cost[i]
            tank = tank + gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0
        if total < 0:
            return -1
        return start
