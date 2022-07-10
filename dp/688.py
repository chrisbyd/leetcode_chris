

import re
from shutil import move

# dfs will TLE error
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2,-1), (-1,-2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        def dfs(i, j, moves, prob):
  
            if  (i >= n or i < 0 or j >= n or j < 0):
                return 0 
            elif moves == k:
                return prob
            else:
                ans = 0
                for a, b in directions:
                    ans += dfs(i+a, j +b, moves+1, prob * 1/8)
                return ans
        return dfs(row, column, 0, 1.0)

sol = Solution()

n = 8
k = 30
row = 6
column = 4
res = sol.knightProbability(n, k, row, column)
print(res)

# with memory
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2,-1), (-1,-2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

        memo = {}
        def dfs(i, j, moves, prob):
            if (i, j, moves) not in memo:
                if  (i >= n or i < 0 or j >= n or j < 0):
                    res =  0 
                elif moves == k:
                    res = prob
                else:
                    ans = 0
                    for a, b in directions:
                        ans += dfs(i+a, j +b, moves+1, prob * 1/8)
                    res = ans
                memo[i, j, moves] = res
                return res
            else:
                return memo[i, j, moves]
        return dfs(row, column, 0, 1.0)
sol = Solution()

n = 8
k = 30
row = 6
column = 4
res = sol.knightProbability(n, k, row, column)
print(res)