from typing import List
##
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        @lru_cache(None)
        def dp(n):
            if n == 0: return nums[0]
            else:
                ans = []
                for i in range(1,  k+1):
                    if n - i >= 0:
                        ans.append(dp(n - i))
                return max(ans) + nums[n]
        return dp(len(nums) - 1)



### try with bottom up dp
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            ans = -float('inf')
            for j in range(1, k+1):
                if i - j <0: break
                else: 
                    ans = max(ans, dp[i - j])
            dp[i] = ans + nums[i]
        return dp[-1]
                
####bottom up dp with priority queue
###o(n) complexity
from heapq import heappush, heappop

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        heap = [(- nums[0], 0)]
        for i in range(1, len(nums)):
            while heap[0][1] < i - k:
                heappop(heap)
            ans, _ = heap[0]
            dp[i] = - ans + nums[i]
            heappush(heap,(- dp[i], i))
        return dp[-1]
                
            
        
            