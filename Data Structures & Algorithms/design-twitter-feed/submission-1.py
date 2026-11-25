from collections import defaultdict
from heapq import heappush as insert
from heapq import heappop as delete
class Tweet:
    def __init__(self, id, tweetId, userId):
        self._id = id
        self._tweetId = tweetId
        self._userId = userId
    
    def __lt__(self, other):
        return self._id > other._id

class Twitter:

    def __init__(self):
        self.tweet_count = 0
        self._follow = defaultdict(set)
        self.user_to_tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = Tweet(self.tweet_count, tweetId, userId)
        self.tweet_count += 1
        self.user_to_tweets[userId].append(tweet)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        
        followeeIdList = [userId]
        if userId in self._follow and  self._follow[userId]:    
            followeeIdList += list(self._follow[userId])

        print(userId)
        print(followeeIdList)

        heap = []

        for i in range(len(followeeIdList)):
            for tweet in self.user_to_tweets[followeeIdList[i]]:
                insert(heap, tweet)

        res = []

        while heap and len(res) < 10:
            res.append(delete(heap)._tweetId)
    
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self._follow[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self._follow and followeeId in self._follow[followerId]:
            self._follow[followerId].remove(followeeId)


        
