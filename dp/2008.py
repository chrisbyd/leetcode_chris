from typing import List

import bisect

##### not accepted because of time limit
## still not the optimal
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides = sorted(rides)

        m = len(rides)
        start_index = [rides[i][0] for i in range(m)]
        #@lru_cache(None)
        def dp(rides_index):
            if rides_index == m:
                return 0
            ans = - float('inf')
            for r_index, (start, end, tip) in enumerate(rides[rides_index:]):
                print(start, end, tip)
                print("dp index is", rides_index)
                if start < rides[rides_index][1]:
                    r_index = bisect.bisect_left(start_index, end)
                    ans = max(ans, end - start + tip + dp(r_index))
            
            return ans
        return dp(0)


### 


sol = Solution()
n = 10
rides = [[2,3,6],[8,9,8],[5,9,7],[8,9,1],[2,9,2],[9,10,6],[7,10,10],[6,7,9],[4,9,7],[2,3,1]]
res = sol.maxTaxiEarnings(n, rides)
print(res)

#### try another solution
from collections import defaultdict
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        @lru_cache(None)
        def f(i):
            if i==n:return 0
            ans=f(i+1)
            for j,k in x[i]:
                ans=max(ans,j-i+k+f(j))
            return ans
        x=defaultdict(list)
        for a,b,c in rides:
            x[a].append((b,c))
        return f(1)