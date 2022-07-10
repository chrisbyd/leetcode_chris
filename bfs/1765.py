from typing import Optional, List
import copy
from collections import deque

class Solution:
    def checkValid(self, x, y, matrix):
        m, n = len(matrix), len(matrix[0])
        if x >=0 and x < m and y >= 0 and y < n and matrix[x][y] == 0:
            return True
        return False
            
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[0] * n for i in range(m)]
        q = deque([])
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append([i, j])
                    
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        value = 0
        
        while q:
            length = len(q)
     
            for i in range(length):
                x, y = q.popleft()
                height[x][y] = value
                for x1, y1 in directions:
                    if self.checkValid(x+ x1, y+ y1, isWater):
                        isWater[x+ x1][y+ y1] = 2
                        q.append([x+ x1, y + y1])
                        
            value += 1
            
        ans = max([max(height[i]) for i in range(m)])
        
        return height
                        
sol = Solution()
isWater = [[0,1],[0,0]]
res = sol.highestPeak(isWater=isWater)
print(res)
