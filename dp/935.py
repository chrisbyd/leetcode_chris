
from functools import lru_cache
import math
class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [[0 for j in range(10)] for i in range(n)]
        for j in range(10):
            dp[0][j] = 1
        for i in range(1,n):
            for j in range(10):
                if j == 4:
                    dp[i][j] = dp[i-1][3] + dp[i-1][9] + dp[i-1][0]
                elif j == 6:
                    dp[i][j] = dp[i-1][1] + dp[i-1][7] + dp[i-1][0]
                elif j == 0:
                    dp[i][j] = dp[i-1][4] + dp[i-1][6]
                elif j == 1:
                    dp[i][j] = dp[i-1][6] + dp[i-1][8]
                elif j == 2:
                    dp[i][j] = dp[i-1][7] + dp[i-1][9]
                elif j == 3:
                    dp[i][j] = dp[i-1][4]  + dp[i-1][8]  
                elif j == 7:
                    dp[i][j] = dp[i-1][2] + dp[i-1][6]
                elif j == 8:
                    dp[i][j] = dp[i-1][1] + dp[i-1][3]
                elif j == 9:
                    dp[i][j] = dp[i-1][4] + dp[i-1][2]
        return sum(dp[-1]) % (10**9 + 7)


sol = Solution()
n = 3131
res = sol.knightDialer(n)
print(res)


### dfs algorithm
####it should also be pretty easy to solve with dfs

class Solution:
    def knightDialer(self, n: int) -> int:
        reachable = {
            1 : [8, 6],
            2 : [7, 9],
            3 : [4, 8],
            4 : [3, 9, 0],
            5 : [],
            6 : [7, 1, 0],
            7 : [2, 6],
            8 : [1, 3],
            9 : [4, 2],
            0 : [4, 6]
        }
        memo = {}
        def dfs(n, digit):
            if (n, digit) in memo:
                return memo[n, digit]
            else: 
                if n == 1:
                    memo[n, digit] = 1
                    return 1
                else:
                    ans = 0
                    for n_digit in reachable[digit]:
                        ans += dfs(n-1, n_digit)
                    memo[n, digit] = ans
                    return ans
        ans = 0
        for i in range(10):
            ans += dfs(n, i)
        return ans % (10 ** 9 + 7)

sol = Solution()
n = 3131
res = sol.knightDialer(n)
print(res)

