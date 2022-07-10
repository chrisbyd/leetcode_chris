from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [ [0 for j in range(n+2)] for i in range(m+2)]
        largest = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) +1
                    if dp[i+1][j+1] > largest:
                        largest = dp[i+1][j+1]

 
        return largest * largest

sol = Solution() 

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["0","1"],["1","0"]]
res = sol.maximalSquare(matrix)
print(res)

        