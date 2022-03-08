from typing import List
# backtracking
#time limit exceeded
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(coins, target):
            if target == 0:
                return 0
            elif min(coins) > target:
                return 999999
            elif min(coins) == target:
                return 1
            else:
                res = []
                for coin in coins:
                    out = dp(coins, target - coin) + 1
                    res.append(out)
                return  min(res)
       
        res = dp(coins, amount)
        if res >= 999999:
            return -1
        return res

sol = Solution()

coins = [1,2]
amount = 2
res = sol.coinChange(coins, amount)
print(res)
        

# top down  dynamic programming
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(coins, remain, count):
            if remain < 0:
                return -1
            if remain == 0:
                return 0 
            if count[remain] != 0:
                return count[remain]
            else:
                minimum = float('inf')
                for coin in coins:
                    res = dp(coins, remain - coin, count)
                    if res >=0 and res < minimum:
                        minimum = res 
            
                count[remain] = -1 if minimum == float('inf') else minimum +1
                return count[remain]
        if amount < 1:
            return 0
        return dp(coins, amount, [0 for i in range(amount+1)])

sol = Solution1()

coins = [1,2]
amount = 2
res = sol.coinChange(coins, amount)
print(res)
            
# bottom up dynamic programming
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        coins.sort()
        for coin in coins:
            for j in range(coin, amount +1):
                dp[j] = min(dp[j], 1 + dp[j - coin])
        return dp[amount] if dp[amount] != float('inf') else -1



sol = Solution2()

coins = [1,2,5]
amount = 11
res = sol.coinChange(coins, amount)
print(res)
            


       