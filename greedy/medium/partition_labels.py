"""
763. Partition Labels
"""
from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        static = {}
        end = 0
        ans = []
        start = 0
        for i, j in enumerate(s):
            static[j] = i

        for k in range(len(s)):
            end = max(static[s[k]], end)
            if k == end:
                ans.append(k-start+1)
                start = k + 1
        return ans
