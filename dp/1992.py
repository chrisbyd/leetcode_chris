from typing import List
from collections import defaultdict
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        dp = defaultdict(list)
        m, n = len(land), len(land[0])
        new_land = [[0 for j in range(n+2)] for i in range(m+2)]
        for i in range(m):
            for j in range(n):
                new_land[i+1][j+1] = land[i][j]
        for i in range(m+2):
            for j in range(n+2):
                if new_land[i][j] == 1:
                    dp[i,j] = [1,1]
                    if new_land[i-1][j] == 1:
                        dp[i,j] = [dp[i-1, j][0] + 1, dp[i-1, j][1]]
                    if new_land[i][j-1] == 1:
                        dp[i,j] = [dp[i, j-1][0] , 1 + dp[i, j-1][1]]
        ans = []
        for i in range(m+2):
            for j in range(n+2):
                if new_land[i][j] == 1 and  new_land[i+1][j] == 0 and new_land[i][j+1] == 0:
                        ans.append([ i - dp[i,j][0], j - dp[i,j][1], i-1, j-1])
        return ans


sol = Solution()
land = [[1,0,0],[0,1,1],[0,1,1]]
res = sol.findFarmland(land)
print(res)


### using dfs to solve
from typing import List
from collections import defaultdict
class Solution:
    def checkValid(self, i, j, land):
        m,  n = len(land), len(land[0])
        if i >= 0 and i < m and j >=0 and j < n and land[i][j] == 1:
            return True
        return False
        
    def dfs(self, i, j, land, bottom):
        if not self.checkValid(i, j, land):
            return
        else:
            bottom[0] = max(i, bottom[0])
            bottom[1] = max(j, bottom[1])
            land[i][j] = 2
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                self.dfs(i+x, j+y, land, bottom)
                
    
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1: 
                    top = [i, j]
                    bottom = [-1, -1]
                    self.dfs(i, j, land, bottom)
                    coord = top + bottom
                    ans.append(coord)
        return ans
                


        
                        
        
        
        
        
        