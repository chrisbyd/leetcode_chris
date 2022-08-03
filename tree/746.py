from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def dp(i):
            if i == 0 or i == 1:
                return 0
            else:
                return min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
        length = len(cost)
        return dp(length)
            