from typing import List


# class UnionFind:
#     def __init__(self, length):
#         self.parent = [i for i in range(length)]
    
    
#     def union(self, i, j):
#         self.parent[self.root(j)] = self.parent[self.root(i)]

#     def find(self, i, j):
#         r_i = self.root(i)
#         r_j = self.root(j)
#         if r_i == r_j:
#             return True
#         return False
 
#     def root(self, i):
#         if self.parent[i] == i:
#             return i
#         else:
#             return self.root(self.parent[i])


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m, n = len(grid), len(grid[0])
#         UF = UnionFind(m*n)
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1' and i>0 and grid[i-1][j] == '1':
#                     UF.union(i*n+j, i*n +j -n)
#                 if grid[i][j] == '1' and j>0 and grid[i][j-1] == '1':
#                     UF.union(i*n+j, i*n + j-1)
#                 if grid[i][j] == '1' and j<n-1 and grid[i][j+1] == '1':
#                     UF.union(i*n+j, i*n + j+1)
#                 if grid[i][j] == '1' and i<m-1 and grid[i+1][j] == '1':
#                     UF.union(i*n+j, i*n + j +n)
        
#         root = []
#         islands = 0
#         for i in range(m):
#             for j in range(n):
#                 index = i *n + j
#                 if grid[i][j] == '1':
#                     t_root = UF.root(index)
#                     if t_root not in root:
#                         root.append(t_root)
#                         islands += 1
        
#         return islands



# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
# sol = Solution()

# res = sol.numIslands(grid)
# print(res)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        num_islands = 0 
        visited = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i,j):
            if i < 0 or i > m-1 or j < 0 or j > n-1 or grid[i][j] == '0' or visited[i][j] == 1:
                return
            visited[i][j] = 1
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for a, b in directions:
                dfs(i+a, j+b)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    dfs(i,j)
                    num_islands +=1
        return num_islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
#grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
sol = Solution()

res = sol.numIslands(grid)
print(res)


