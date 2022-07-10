from typing import List

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        @lru_cache(None)
        def dp(n):
            if n == 1:
                return 1
            elif n == 2:
                return 0.50
            else:
                return 1/n + (n-2)/n * dp(n-1)
        return dp(n)
        
        
        