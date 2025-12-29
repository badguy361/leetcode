"""
621. Task Scheduler
"""
from typing import List
import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_task = Counter(tasks)
        maxHeap = [-c for c in count_task.values()]
        heapq.heapify(maxHeap)
        cooldown = deque()
        time = 0
        while maxHeap or cooldown:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt != 0:
                    cooldown.append((time + n, cnt))

            if cooldown and cooldown[0][0] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[1])
        return time
