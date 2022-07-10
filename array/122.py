
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        tot_profit = 0
        buy_price = prices[0]
        
        for i in range(1,len(prices)):
            if prices[i] > buy_price:
                tot_profit += prices[i] - buy_price
            buy_price = prices[i]
            print(buy_price)
        return tot_profit
    
sol = Solution()
prices = [7,1,5,9,10]
res = sol.maxProfit(prices)
print(res)
        
             

