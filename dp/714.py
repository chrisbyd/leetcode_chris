import re
from typing import List

# it did not [pass] I dont know know
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ans = []
        for i in range(len(prices) - 1):
            if prices[i+1] - prices[i] >0 :
                if ans and  prices[i+1]- ans[-1][0] > ans[-1][1] - ans[-1][0] + prices[i+1] - prices[i] -fee:
                    new_left = ans[-1][0]
                    ans.pop()
                    ans.append([new_left, prices[i+1]])
                else:
                    ans.append([prices[i], prices[i+1]])
        res = 0
        for interval in ans:
            to_add = max(interval[1] - interval[0] - fee, 0)
            res += to_add
        return res 

sol = Solution()
prices = [1,3,2,8,4,9]
prices = [4,5,2,4,3,3,1,2,5,4]
prices = [2,2,1,1,5,5,3,1,5,4]
fee = 2
res = sol.maxProfit(prices, fee)
print(res)

# dynamic programming is easy to solve this problem
#so for every
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sold, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            hold = max(hold, sold-prices[i])
            sold = max(sold, hold + prices[i] - fee)

        return sold


sol = Solution()
prices = [1,3,2,8,4,9]
prices = [4,5,2,4,3,3,1,2,5,4]
prices = [2,2,1,1,5,5,3,1,5,4]
fee = 2
res = sol.maxProfit(prices, fee)
print(res)




        
