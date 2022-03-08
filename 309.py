from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [[-1 for _ in range(2)] for _ in range(n)]
        def dp(pos, state):
            if pos >= n:
                return 0
            if memo[pos][state] != -1:
                return memo[pos][state]
            # u could buy or cooldown
            elif state == 0:
                mp = max(dp(pos+1, 1) - prices[pos], dp(pos+1, 0))
            elif state == 1:
                mp = max(dp(pos+2, 0) + prices[pos], dp(pos+1 ,1))
            memo[pos][state] = mp
            return mp
        
        res = dp(0, 0)
        return res 
    
sol = Solution()
prices = [1,2,3,0,2]
res = sol.maxProfit(prices)
print(res)
             

        


        