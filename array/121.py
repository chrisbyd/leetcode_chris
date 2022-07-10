
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 999999
        price = 9999999
        mp = 0
        for value in prices:
            if value < buy:
                buy = value
            tp = value - buy
            if tp > mp:
                mp = tp
        return mp



prices  = [2,1,2,1,0,1,2]
prices = [7,1,5,3,6,4]
sol = Solution()
res = sol.maxProfit(prices)
print(res)