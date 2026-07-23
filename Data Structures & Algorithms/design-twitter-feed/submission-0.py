from collections import defaultdict
import heapq
from typing import List
class Twitter:

    def __init__(self):
        
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        heap = []

        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                timestamp, tweet_id = self.tweets[uid][index]

                heapq.heappush(heap, (-timestamp, tweet_id, uid, index))
        
        news_feed = []

        while heap and len(news_feed) < 10:

            neg_timestamp, tweet_id, uid, index = heapq.heappop(heap)

            news_feed.append(tweet_id)

            if index > 0 :
                new_index = index - 1
                new_timestamp, new_tweet_id = self.tweets[uid][new_index]

                heapq.heappush(heap, (-new_timestamp, new_tweet_id, uid, new_index))


        return news_feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
