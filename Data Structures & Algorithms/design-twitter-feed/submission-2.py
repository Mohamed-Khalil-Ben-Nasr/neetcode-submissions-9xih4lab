class User:
    def __init__(self, userId : int):
        self.userId = userId
        self.userPosts = []
        self.following = {}

class Post:
    def __init__(self, tweetId : int, timePosted: int):
        self.tweetId = tweetId
        self.timePosted = timePosted

class Twitter:
    # orchastrator
    def __init__(self):
        self.users = {}
        # assuming no concurrency
        self.logicalClock = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)
        currentUser = self.users[userId]
        newPost = Post(tweetId, self.logicalClock)
        currentUser.userPosts.append(newPost)
        self.logicalClock += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.users[userId] = User(userId)
        currentUser = self.users[userId]
        posts = []
        posts.extend(currentUser.userPosts)
        for f in currentUser.following.values():
            posts.extend(f.userPosts)
        sortedPosts = []
        for post in posts:
            sortedPosts.append([post.tweetId, post.timePosted])
        sortedPosts.sort(key = lambda post : post[1])
        print(sortedPosts)
        res = deque([])
        i = len(posts)-1
        ps = 10
        while i >= 0 and ps > 0:
            res.append(sortedPosts[i][0])
            print(res)
            ps -= 1
            i -= 1
        return list(res)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        follower = self.users[followerId]
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        followee = self.users[followeeId]
        if followeeId not in follower.following:
            follower.following[followeeId] = followee

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        follower = self.users[followerId]
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        followee = self.users[followeeId]
        if followeeId in follower.following:
            del follower.following[followeeId]
