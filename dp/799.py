
# my solution of simulation is way more complex
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for j in range(i+1)] for i in range(query_row + 1)]
        dp[0][0] = [poured, 0] if poured <= 1 else [1, poured -1]
        for row in range(1, query_row+1):
            for column in range(row + 1):
                if column == 0:
                    if  1/2 * dp[row-1][0][-1] <= 1:
                        current = 1/2 * dp[row-1][0][-1]
                        excess = 0
                    else:
                        current = 1
                        excess = 1/2 * dp[row-1][0][-1] -1
                elif column == row:
                    if 1/2 * dp[row-1][-1][-1] <= 1:
                        current = 1/2 * dp[row-1][0][-1]
                        excess = 0
                    else:
                        current = 1
                        excess = 1/2 * dp[row-1][-1][-1] -1
                else:
                    res = 1/2 * dp[row -1][column -1][-1] + 1/2 * dp[row -1][column][-1]
                    if res <= 1:
                        current = res
                        excess = 0
                    else:
                        current = 1
                        excess = res - 1
                dp[row][column] = [current, excess]
      
        return dp[-1][query_glass][0]

sol =  Solution()
poured = 100000009
query_row = 33
query_glass = 17
res = sol.champagneTower(poured, query_row, query_glass)
print(res)

#the standard solution of simulation
#import xrange
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        A  = [[0] * k for k in range(1,102)]
        A[0][0] = poured
        for r in range(query_row +1):
            for c in range(r+1):
                excess = (A[r][c] - 1.0) / 2.0
                if excess > 0:
                    A[r+1][c] += excess
                    A[r+1][c+1] += excess
        return min(1, A[query_row][query_glass])



sol =  Solution()
poured = 100000009
query_row = 33
query_glass = 17
res = sol.champagneTower(poured, query_row, query_glass)
print(res)



                






        