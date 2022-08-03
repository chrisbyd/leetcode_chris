from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for money in accounts:
            ans = max(ans, sum(money))
        return ans
            
        