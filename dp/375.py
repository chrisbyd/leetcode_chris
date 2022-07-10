
from functools import lru_cache
from tkinter.messagebox import NO


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == j :
                return 0
            elif j < i:
                return 0
            else:
                ans = float('inf')
                for index in range(i, j+1):
                    ans = min(ans, max(index + dp(index+1, j), index + dp(i , index -1)))
                return ans
        return dp(1, n)

sol = Solution()
n = 10
res = sol.getMoneyAmount(n)
print(res)

        