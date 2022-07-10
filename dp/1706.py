from  typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        new_grid = [[0]* (n+2) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                new_grid[i][j+1] = grid[i][j]
        dp = [[-1] *(n+2) for i in range(m+1)]
        for j in range(1, n+1):
            dp[-1][j] = j-1
        for i in range(m-1, -1, -1):
            for j in range(1, n+1):
                if new_grid[i][j] == 1 and new_grid[i][j+1] == 1:
                    dp[i][j] = dp[i+1][j+1]
                elif new_grid[i][j] == -1 and new_grid[i][j-1] == -1:
                    dp[i][j] = dp[i+1][j-1]
        return dp[0][1: -1]
        
        
        