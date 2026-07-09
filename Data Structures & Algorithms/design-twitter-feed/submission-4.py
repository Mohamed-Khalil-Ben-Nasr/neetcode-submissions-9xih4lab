from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.userIdToFollowers = defaultdict(set)
        self.userIdToTweets = defaultdict(list)
        self.logicalClock = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userIdToTweets[userId].append([-self.logicalClock , tweetId])
        self.logicalClock += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        for followedId in self.userIdToFollowers[userId]:
            if len(self.userIdToTweets[followedId]) > 0:
                time, mostRecentPostId = self.userIdToTweets[followedId][-1]
                postIndex = len(self.userIdToTweets[followedId])-1
                heapq.heappush(heap, [time, mostRecentPostId, followedId, postIndex])
        # add current user's most recent post to heap too
        if self.userIdToTweets[userId]:
            time, pid = self.userIdToTweets[userId][-1]
            pIndex = len(self.userIdToTweets[userId])-1
            heapq.heappush(heap, [time, pid, userId, pIndex])
        # now we created a heap using each followed user's most recent tweet
        # (including oneself)
        res = []
        while len(res) < 10 and heap:
            # pop most recent post and add it to result
            time, pid, userId, pIndex = heapq.heappop(heap)
            res.append(pid)
            # push same user's next most recent post to heap
            # so that heap is always of size k
            if pIndex - 1 >= 0:
                newTime, newTweetId = self.userIdToTweets[userId][pIndex - 1]
                heapq.heappush(heap, [newTime, newTweetId, userId, pIndex-1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId in self.userIdToFollowers[followerId]:
            return
        self.userIdToFollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.userIdToFollowers[followerId] :
            return
        self.userIdToFollowers[followerId].remove(followeeId)
