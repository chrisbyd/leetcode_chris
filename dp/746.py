from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for i in range(n+1)]
        if len(cost) <= 2:
            return min(cost)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]

sol = Solution()
cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
cost 
res = sol.minCostClimbingStairs(cost)
print(res)