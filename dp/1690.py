from functools import lru_cache
from multiprocessing.connection import answer_challenge
from typing import List
import math

## time limit exceeds
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j, player, cur_sum):
            if i == j:
                return cur_sum
            else:
                if player == 0:
                    a =   dp(i+1, j, 1 - player,sum(stones[i+1:j+1]) + cur_sum)
                    b = dp(i, j-1, 1- player, sum(stones[i:j]) + cur_sum) 
                    ans = max(a, b, key= abs)
                else:
                    a =  dp(i+1, j, 1 - player, cur_sum -sum(stones[i+1:j+1]))
                    b =   dp(i, j-1, 1- player, cur_sum -sum(stones[i:j])) 
                    ans = min(a, b, key= abs)
                return ans
        return dp(0, len(stones)-1, 0, 0)

sol = Solution()
stones = [5,3,1, 4, 2]
stones = [792,195,697,271,743,51,836,322,135,550,399,182,988,25,395,254,480,931,513,772,798,102,110,915,794,330,597,220,789,462]
stones =  [7,90,5,1,100,10,10,2]
res = sol.stoneGameVII(stones)
print(res) 


## another solution provided by youtube
###  always maximize the relative score no matter who's playing the game maxm  ax
#### 区间性dp
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 0
   
        dp[0][1] = 1
     
        for m in range(1,n):
            for i in range(n - m): 
              
                dp[i][i+m] = max(sum(stones[i+1:i+m+1]) - dp[i+1][i+m], sum(stones[i:i+m]) - dp[i][i+m-1])
          
        return dp[0][-1]



sol = Solution()
stones = [5,3,1, 4, 2]

res = sol.stoneGameVII(stones)
print(res) 



        

## another solution provided by youtube
###  always maximize the relative score no matter who's playing the game maxm  ax
#### 区间性dp
#### 区间和的解法！！
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 0
   
        dp[0][1] = 1

        sum = 0
        cum_sum = [0 for i in range(n+1)]
        for idx, stone in enumerate(stones):
            sum += stone
            cum_sum[idx+1] = sum
      
        for m in range(1,n):
            for i in range(n - m): 
             
                dp[i][i+m] = max(cum_sum[i+m+1] - cum_sum[i+1] - dp[i+1][i+m], cum_sum[i+m] - cum_sum[i] - dp[i][i+m-1])
             
        return dp[0][-1]

sol = Solution()
stones = [5,3,1, 4, 2]
stones = [481,905,202,250,371,628,92,604,836,338,676,734]
stones = [7,90,5,1,100,10,10,2]
res = sol.stoneGameVII(stones)
print(res) 

         

        
