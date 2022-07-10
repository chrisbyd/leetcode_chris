import re
from typing import List
# with memory
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if i == 0:
                    res = triangle[i][0]
                elif j == 0:
                    res = dp(i-1, j) + triangle[i][j] 
                elif j == i:
                    res =  dp(i-1, j-1) + triangle[i][j]
                else:
                    res = min(dp(i-1, j), dp(i-1, j-1)) + triangle[i][j]
                memo[i, j] = res
                return res
            else:
                return memo[i, j]
        ans = float('inf')
        m = len(triangle)
        for j in range(m ):
            ans = min(ans, dp(m-1, j))
        
        return ans

sol = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
res = sol.minimumTotal(triangle)
print(res)    


# with bottom up dynamic programming

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp, m = [[0 for j in range(i+1)] for i in range(len(triangle))] , len(triangle)
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[-1])

sol = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
res = sol.minimumTotal(triangle)
print(res)    