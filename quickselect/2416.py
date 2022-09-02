from typing import List
from collections import deque
from heapq import heappop, heappush
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        heap = [(0, grid[start[0]][start[1]], start[0], start[1])]
        ans = []
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        visited = set()
        distance = 0
        while heap:
            distance += 1
            length = len(heap)
            for _ in range(length): 
                dis, price , i, j = heappop(heap)
                visited.add((i, j))
                if price <= pricing[1] and price >= pricing[0] and price != 1:
                    ans.append([i, j])
                    k-= 1
                    if k <= 0:
                        return ans
                for ii, jj in directions:
                    if (i+ ii, j+ jj) in visited: 
                        continue
                    if i+ ii >= m or i+ ii < 0 or j + jj >= n or j+jj < 0:
                        continue
                    elif grid[i+ii][j+jj] == 0 :
                        continue
                    else:
                        visited.add((i+ii, j+ jj))
                        nprice = grid[i+ii][j+jj]
                        heappush(heap, (distance, nprice, i+ii, j+ jj))
        return ans
                
sol = Solution()
grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]]
pricing = [2,5]
start = [0,0]
k = 3
grid = [[0,2,0]]
pricing = [2,2]
start = [0,1]
k = 1
res = sol.highestRankedKItems(grid, pricing, start, k)
print(res)

                    