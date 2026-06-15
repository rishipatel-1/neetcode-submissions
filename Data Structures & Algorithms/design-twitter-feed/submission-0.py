import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0

        self.tweets = {}

        self.followMap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append(
            (self.time, tweetId)
        )

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []

        maxHeap = []

        followees = self.followMap.get(userId, set()).copy()

        followees.add(userId)

        for user in followees:

            if user in self.tweets:

                index = len(self.tweets[user]) - 1

                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    maxHeap,
                    (-time, tweetId, user, index)
                )

        while maxHeap and len(res) < 10:

            negTime, tweetId, user, index = heapq.heappop(maxHeap)

            res.append(tweetId)

            index -= 1

            if index >= 0:

                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    maxHeap,
                    (-time, tweetId, user, index)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.followMap:
            self.followMap[followerId] = set()

        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.followMap:

            self.followMap[followerId].discard(followeeId)