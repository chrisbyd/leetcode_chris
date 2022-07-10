
from functools import lru_cache

# top down approach
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1
        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b > 0:
                return 1
            elif a <=0 and b<= 0:
                return 1 * 0.5
            elif a >0 and b <= 0:
                return 0
            else:
                ans = 0.25 * dp(a-100, b) + 0.25 * dp(a-75, b -25) + 0.25 * dp(a-50, b-50) \
                    + 0.25 * dp(a-25, b-75)
                return ans
        return dp(n,n)

sol = Solution()
n = 800
res = sol.soupServings(n)
print(res)

##solution with bottom up approach
class Solution:
    def soupServings(self, n: int) -> float:
        