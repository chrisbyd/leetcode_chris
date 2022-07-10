from typing import List
##

#### easy dfs solution
class Solution:
    def checkValid(self, i, j, grid2):
        m, n = len(grid2), len(grid2[0])
        if i >= 0 and i < m and j >= 0 and j < n and grid2[i][j] == 1:
            return True
        return False
    
    def dfs(self, i, j, grid1, grid2):
        if not self.checkValid(i, j, grid2):
            return 0
        else:
            ans = 0
            grid2[i][j] = 2
            if grid1[i][j] != 1:
                ans = 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                ans += self.dfs(i+x, j+y, grid1, grid2)
            return ans
            
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res = self.dfs(i, j, grid1, grid2)
                    if res == 0:
                        ans += 1
        return ans
                    