from typing import List
### a simple dynamic programming method
import sys
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = {}
        def dp(row, endColumn):
            if (row, endColumn) not in cache:
                if row == 0:
                    ans = grid[0][endColumn]
                else:
                    ans = float('inf')
                    for j in range(n):
                        prev_value = grid[row -1][j]
                        this_value = grid[row][endColumn]
                        ans = min(ans, dp(row -1, j) + this_value + moveCost[prev_value][endColumn])
                cache[row, endColumn] = ans
                return ans
            else:
                return cache[row, endColumn]
        ans = sys.maxsize
        for i in range(n):
            ans = min(dp(m-1, i), ans)
        return ans

### solve with bottom up dymamic programming
import sys
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for i in range(m)]
        for j in range(n):
            dp[0][j] = grid[0][j]
        for i in range(1, m):
            for j in range(n):
                ans = sys.maxsize
                this_value = grid[i][j]
                for k in range(n):
                    prev_value = grid[i-1][k]
                    ans = min(ans, dp[i-1][k] + moveCost[prev_value][j])
                dp[i][j] = ans + this_value
        return min(dp[-1])
                    
            
      

                    