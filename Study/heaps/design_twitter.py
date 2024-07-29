"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to
see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object. void postTweet(int userId, int tweetId) Composes a new tweet with ID
tweetId by the user userId. Each call to this function will be made with a unique tweetId. List<Integer> getNewsFeed(
int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted
by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent. void
follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID
followeeId.


Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation Twitter twitter = new Twitter(); twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2. twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should
precede tweet id 5 because it is posted after tweet id 5. twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer
following user 2.

Link: https://leetcode.com/problems/design-twitter/

"""


class Twitter:

    def __init__(self):
        self.followMap = collections.defaultdict(set)
        self.tweetMap = collections.defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1  # Since we can only use minHeap in python

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []

        self.followMap[userId].add(userId)
        # Get the most recent tweet from the users that are valid (following + user himself)
        # Add userId and index - 1 to point to the next recent value for that particular user
        # So it can be picked and pushed in the heap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([time, tweetId, followeeId, index - 1])

        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, prev_index = heapq.heappop(minHeap)
            res.append(tweetId)
            if prev_index >= 0:
                # Checking for the next recent tweet from the same user
                time, tweetId = self.tweetMap[followeeId][prev_index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, prev_index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
