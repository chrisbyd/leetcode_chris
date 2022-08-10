from typing import List
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_sum = [[0 for j in range(n+1)] for i in range(m+1)]
        col_sum = [[0 for j in range(n+1)] for i in range(m+1)]
        dig_sum = [[0 for j in range(n+1)] for i in range(m+1)]
        dig1_sum = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                row_sum[i+1][j+1] += grid[i][j] + row_sum[i+1][j]
                col_sum[i+1][j+1] += grid[i][j] + col_sum[i][j+1]
                dig_sum[i+1][j+1] +=  grid[i][j] + dig_sum[i][j]
                dig1_sum[i+1][j] +=  grid[i][j] + dig1_sum[i][j+1]
      
  
        def checkMagic(x, y, side):

            t_sum = dig_sum[x][y] -dig_sum[x-side][y-side]
            for i in range(side):
                c_sum = col_sum[x][y - i] - col_sum[x - side][y-i]
                r_sum = row_sum[x- i][y] - row_sum[x- i][y - side]
                if c_sum != t_sum or r_sum != t_sum:
                    return False
            t1_sum = dig1_sum[x][y-side] - dig1_sum[x - side ][y]
          
            return t_sum == t1_sum
        maxlen = 0
        for i in range(1, m +1):
            for j in range(1, n+1):
                length = min(i, j)
                if n <= maxlen:
                    continue
                for s in range(1, length +1):
                    if s <= maxlen:
                        continue
                    elif checkMagic(i, j, s ):
                        maxlen = max(maxlen, s)
        return maxlen
sol = Solution()
grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
res =  sol.largestMagicSquare(grid)
print(res)