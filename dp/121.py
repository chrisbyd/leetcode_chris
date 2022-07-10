from typing import List


# two pointer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        ans = 0
        for value in prices:
            if value < buy:
                buy = value
            profit = value - buy
            if profit > ans:
                ans = profit 
        return ans 
sol = Solution()
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
res = sol.maxProfit(prices)
print(res)



        