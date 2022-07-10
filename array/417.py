from typing import List
import collections
from collections import deque

#bfs algorithm

class Solution:
    def pacificAtlantic(self, heights) :
        m, n = len(heights), len(heights[0])
        pacific, atlantic = deque(), deque()
        for i in range(m):
            pacific.append((i, 0, heights[i][0]))
            atlantic.append((i, n-1, heights[i][n-1]))
        for j in range(n):
            pacific.append((0,j, heights[0][j]))
            atlantic.append((m-1, j, heights[m-1][j]))
        
        def bfs(ocean):
            visited = [[0 for j in range(n)] for i in range(m)]
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            ans_set = set()
            while ocean:
                i, j, value = ocean.popleft()
                visited[i][j] = 1
                ans_set.add((i,j))
                for a, b in directions:
                    if a + i >= 0 and a +i < m and b +j >= 0 and b+j < n and value <= heights[i+a][j+b] and visited[i+a][j+b] == 0:
                        ocean.append((i+a, j+b ,heights[i+a][j+b]))
              
            return ans_set
        
        return list(bfs(pacific) & bfs(atlantic))

sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
res = sol.pacificAtlantic(heights)
print(res)

                        




                    



        














