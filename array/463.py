from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        new_grid = [[0 for j in range(n+2)] for i in range(m+2)]
        for i in range(m):
            for j in range(n):
                new_grid[i+1][j+1] = grid[i][j]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0
        for i in range(m+1):
            for j in range(n+1):
                if new_grid[i][j] == 1:
                    for a,b in directions:
                        if new_grid[i+a][j+b] == 0:
                            ans += 1
        
        return ans


sol = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
res = sol.islandPerimeter(grid)
print(res)