from typing import List
###accepted 
import bisect
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        startTime = [events[i][0] for i in range(n)]
        @lru_cache(None) 
        def dp(index,maximum):
       
            if index == n or maximum == 2:
                return 0
            else:
                ans = 0
                idx1 = bisect.bisect_left(startTime, events[index][1] + 1 )
                ans = max(ans, events[index][2] + dp(idx1, maximum +1))
                
                ans = max(ans, dp(index+1, maximum))
          
                return ans
        return dp(0, 0)
                

sol = Solution()
events = [[1,3,2],[4,5,2],[2,4,3]]
res = sol.maxTwoEvents(events)
print(res)