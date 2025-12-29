"""
355. Design Twitter
"""
from typing import List
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follow_table = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = {userId} | self.follow_table[userId]
        maxHeap = []
        for user in users:
            if self.tweets[user]:
                time, tweetId = self.tweets[user][-1]
                idx = len(self.tweets[user]) - 1
                heapq.heappush(maxHeap, (-time, tweetId, user, idx))

        ans = []
        while maxHeap and len(ans) < 10:
            _, tweetId, u, i = heapq.heappop(maxHeap)
            ans.append(tweetId)

            if i > 0:
                t, tid = self.tweets[u][i-1]
                heapq.heappush(maxHeap, (-t, tid, u, i-1))
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_table[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_table[followerId].discard(followeeId)
