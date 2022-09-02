from typing import List
from collections import deque
##TLE
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        tsum = sum([sum(row) for row in grid])
        m, n = len(grid), len(grid[0])
     
        if tsum == 0 or tsum == m * n:
            return -1

        def bfs(i, j):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            distance, visited = 0, set()
            q = deque([(0, i, j )])
            visited.add((i, j))
            while q:
                length = len(q)
                distance += 1
                for _ in range(length):
                    dis , r, c = q.popleft()
                    if grid[r][c] == 1:
                        return dis
                    for ii, jj in directions:
                        ni, nj = r +ii, c + jj
                        if ni >= 0 and ni < m and nj >= 0 and nj < n and (ni, nj) not in visited:
                            visited.add((ni, nj))
                            q.append((distance, ni, nj))
        ans = -float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans = max(ans , bfs(i, j))
        return ans
grid = [[1,0,1],[0,0,0],[1,0,1]]
grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
sol = Solution()
res = sol.maxDistance(grid)
print(res)