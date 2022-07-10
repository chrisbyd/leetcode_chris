from typing import List

import bisect
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if len(days) == 0:
            return 0
        elif len(days) == 1:
            return min(costs)
        n = len(days)
        dp = [0 for i in range(len(days))]
        dp[0] = min(costs)
        for i in range(1,n):
            a1 = dp[i-1] + costs[0]
            index = bisect.bisect_left(days, days[i] - 6)
            a2 = dp[index -1] + costs[1] if index >= 1 else costs[1]
            index1 = bisect.bisect_left(days, days[i] - 29)
            a3 = dp[index1 -1] + costs[2] if index1 >= 1 else costs[2]
            dp[i] = min(a1,a2,a3)
  
        return dp[-1]

sol = Solution()
days = [1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29]
costs = [3, 14, 50]
days = [364]
costs = [3, 3, 1]
res = sol.mincostTickets(days, costs)
print(res)