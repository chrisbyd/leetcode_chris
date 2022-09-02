from collections import  deque
from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n =len(matrix), len(matrix[0])
        q = deque([(m-1, 0)])
        dirs = [ (1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        visited.add((m-1, 0))
        values = set([matrix[m-1][0]])
        while q:        
            if len(values) > 1:
                return False
            values = set()
            length = len(q)
            for _ in range(length):
                i, j = q.popleft()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if ni >= 0 and ni < m and nj >= 0 and nj < n and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        values.add(matrix[ni][nj])
                        q.append((ni, nj))
        return True

sol = Solution()

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
matrix = [[1,2],[2,2]]
res = sol.isToeplitzMatrix(matrix)
print(res)