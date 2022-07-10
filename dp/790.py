

#
import math
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [[0,0,0] for i in range(n)]
        mod = math.pow(10, 9) + 7
        dp[0][0] = 1
        dp[1][0], dp[1][1], dp[1][2] = 2, 1, 1
        for i in range(2, n):
            dp[i][0] =  (dp[i-1][0] + dp[i-2][0] + dp[i-1][1] + dp[i-1][2]) % mod
            dp[i][1] =  ( dp[i-2][0] + dp[i-1][2] )% mod
            dp[i][2] =  (dp[i-2][0] + dp[i-1][1]) % mod
        return int(dp[n-1][0] )

n =  50
sol = Solution()
res = sol.numTilings(n)
print(res)


# another easy type of problems
# how many ways that we can cover a N*2 board using one type of domino (1*2)?
# this is a variant of the problem
class Solution:
    def numTilings(self, n: int) -> int:
        def dp(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                return dp(n-1) + dp(n-2)
        return dp (n)




