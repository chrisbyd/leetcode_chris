from typing import List

class Solution:
    ###dp （from top to bottom 1s, from left to right 1s）
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[(0,0) for _ in range(n)] for _ in range(m)]
        max_len = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dp[i][j] = (0,0)
                else:
                    if max_len == 0:
                        max_len = 1
                    if i == 0 and j == 0:
                        dp[i][j] = (1,1)
                    elif i == 0:
                        dp[i][j] = (1, dp[i][j-1][1] + 1)
                    elif j == 0:
                        dp[i][j] = (dp[i-1][j][0] +1, 1)
                    else:
                        dp[i][j] = (dp[i-1][j][0] + 1, dp[i][j-1][1] + 1) #height and width
                        for k in range(max_len, min(dp[i][j])):
                            if dp[i][j-k][0] >= k+1 and dp[i-k][j][1] >= k+1:
                                max_len = k+1
        return max_len * max_len