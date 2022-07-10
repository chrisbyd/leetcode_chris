from functools import lru_cache
import pstats
from typing import List


# easy dfs + how to remove the duplicates
# thats pretty hard
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(index, amount):
            if amount == 0:
                return 1
            elif amount < 0:
                return 0
            else:
                ans = 0
                for i in range(index, len(coins)):
                    ans += dfs(i, amount - coins[i])
                return ans
        return dfs(0, amount)

# with memorization 
#still tle
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(index, amount):
            
            if amount == 0:
                return 1
            elif amount < 0:
                return 0
            else:
                if (index, amount) not in memo:
                    ans = 0
                    for i in range(index, len(coins)):
                        ans += dfs(i, amount - coins[i])
                    memo[index, amount] = ans
                    return ans
                else:
                    return memo[index, amount]
        return dfs(0, amount)

sol = Solution()
coins = [1,2,5]
amount = 5
res = sol.change(amount= amount, coins= coins)
print(res)




# # with dynamic programming
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[1 for _ in range(n) ] for _ in range(amount + 1)]
        for j in range(n):
            dp[-1][j] = 1
        for j in range(n-1, -1, -1):
            for i in range(amount-1, -1, -1):
                ans = 0
                if i + coins[j] <= amount:
                    ans += dp[i+ coins[j]][j]
                if j < n-1:
                    ans += dp[i][j+1]
                dp[i][j] = ans
        return dp[0][0]


sol = Solution()
coins = [1,2,5]
amount = 5
res = sol.change(amount= amount, coins= coins)
print(res)

        
