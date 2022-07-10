from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
        
        def sum_column(j):
            ans = 0
            for i in range(m):
                ans += grid[i][j]
            return ans

        def flip_column(j):
            for i in range(m):
                grid[i][j] = 1 - grid[i][j]
        

        for j in range(n):
    
            if 2* sum_column(j) < m + 1:
                flip_column(j)
       
        ans = 0
        for i in range(m):
            res = 0
            for j in range(n):
                res = res * 2 + grid[i][j]
            ans += res
    
        return ans

sol = Solution()
grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
res = sol.matrixScore(grid)
print(res)

            
