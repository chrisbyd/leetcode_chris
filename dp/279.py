
# top-down solution
from functools import lru_cache
import math
# still TLe
class Solution:
    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        if n == 1 or int(math.sqrt(n)) == math.sqrt(n):
            return 1
        else:
            snumber = int(math.sqrt(n))
            ans = float('inf')
            for i in range(1, snumber +1):
                ans = min(ans, 1 + self.numSquares(n - i* i))
        return ans


sol = Solution()
n = 52
res = sol.numSquares(n)
print(res)

# try bottom-up dynamic programming
import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [1 for i in range(n+1)]
        for i in range(1,n+1):
            if i == int(math.sqrt(i)) * int(math.sqrt(i)):
                dp[i] = 1
            else:
                s_number = int(math.sqrt(i))
                ans = float('inf')
                for j in range(1, s_number +1):
                    ans = min(ans, dp[i - j * j])
                dp[i] = ans + 1
        return dp[-1]




        