"""
506. Relative Ranks
You are given an integer array score of size n, where score[i] is the 
score of the ith athlete in a competition. All the scores are guaranteed 
to be unique.
The athletes are placed based on their scores, where the 1st place athlete 
is the athlete with the highest score, the 2nd place athlete is the athlete 
with the second highest score, and so on. The placement of each athlete 
determines their rank:
- The 1st place athlete's rank is "Gold Medal".
- The 2nd place athlete's rank is "Silver Medal".
- The 3rd place athlete's rank is "Bronze Medal".
- For the 4th place to the nth place athlete, their rank is their placement 
number (i.e., the 4th place athlete's rank is "4th").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

Constraints:
n == score.length
1 <= n <= 10^4
0 <= score[i] <= 10^6
All the values in score are unique.
"""
# solution 1
"""
做法：
1. 使用堆排序，將分數和索引一起存儲，並按分數降序排序
2. 遍歷排序後的結果，根據索引分配排名
"""
from typing import List
import heapq
class Solution1:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        max_heap = [(-s,i) for i,s in enumerate(score)]
        heapq.heapify(max_heap)
        ans = [0] * len(score)
        for rank in range(len(score)):
            _, index = heapq.heappop(max_heap)
            if rank == 0:
                ans[index] = "Gold Medal"
            elif rank == 1:
                ans[index] = "Silver Medal"
            elif rank == 2:
                ans[index] = "Bronze Medal"
            else:
                ans[index] = str(rank+1)
        return ans

# solution 2
"""
做法：
1. 將分數和索引一起存儲，並按分數降序排序
2. 遍歷排序後的結果，根據索引分配排名
"""
class Solution2:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Create a list of tuples (score, index) and sort it by score in descending order
        sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])

        # Prepare the result list with the same length as score
        ans = [""] * len(score)

        # Assign ranks based on sorted order
        for rank, (index, _) in enumerate(sorted_scores):
            if rank == 0:
                ans[index] = "Gold Medal"
            elif rank == 1:
                ans[index] = "Silver Medal"
            elif rank == 2:
                ans[index] = "Bronze Medal"
            else:
                ans[index] = str(rank + 1)

        return ans
