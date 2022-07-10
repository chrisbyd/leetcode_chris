from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for idx, num in enumerate(matrix[0]):
            dp[0][idx] = num
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    ans = min(dp[i-1][j], dp[i-1][j+1]) 
                elif j == n-1:
                    ans = min(dp[i-1][j], dp[i-1][j-1])
                else:
                    ans = min(dp[i-1][j], dp[i-1][j+1], dp[i-1][j-1])
                dp[i][j] = ans + matrix[i][j]
        return min(dp[-1])

sol = Solution()
matrix = [[2,1,3],[6,5,4],[7,8,9]]
res = sol.minFallingPathSum(matrix)
print(res)




        