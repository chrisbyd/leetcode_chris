from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = matrix.copy()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                else:
                    k = min(i, j)
                    for o in range(1, k+1):
                        if matrix[i][j-o] and matrix[i-o][j] and dp[i-1][j-1] >= o:
                            dp[i][j] += 1
                        else:
                            break
        ans = 0
   
        for i in range(m):
            ans += sum(dp[i])
        return ans
                       