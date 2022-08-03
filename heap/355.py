
from heapq import heappush, heappop
from collections import defaultdict
from typing import List

###my solution is much better
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0
        
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(( self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        following = self.following[userId]
        following.add(userId)
        following = list(following)
    
        curs = [-1] * len(following)
        for index, cur_index in enumerate(curs):
            followeeTweets = self.tweets[following[index]]
            if  len(followeeTweets) + cur_index >= 0:
        
                heappush(heap, (-followeeTweets[cur_index][0], followeeTweets[cur_index][1], index))
        t = 10
       
        ans = []
        print(self.tweets)
        while t > 0 and heap:
            time, tid, index = heappop(heap)
            followeeTweets = self.tweets[following[index]]
            cur_index = curs[index] - 1
            curs[index] -= 1
            if cur_index + len(followeeTweets) >= 0:
                heappush(heap, (-followeeTweets[cur_index][0], followeeTweets[cur_index][1], index))
            ans.append(tid)
            t -= 1
        return ans
            
            
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)