



## exceeds maximun recursion depth
from tkinter.tix import Tree


class Solution:
    def isUgly(self, n: int) -> bool:
       # @lru_cache(None)
        def dp(n):
            if n in {1, 2, 3, 5}:
                return True
            elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
                return False
            else:
                ans = False
                if n % 2 == 0:
                    ans = ans or dp(n // 2)
                if n % 3 == 0:
                    ans = ans or dp(n // 3)
                if n % 5 == 0:
                    ans = ans or dp(n // 5)
                return ans
        return dp(n)
                
sol = Solution()
n = 60
res = sol.isUgly(n)
print(res)


### we could solve it with bottom up dynamic programming
#### memory exceeded
#### my solution is way too complicated. It could be much easier
class Solution:
    def isUgly(self, n: int) -> bool:
        if n in {1,2,3,4,5}:
            return 1
        if n <= 0:
            return 0
        dp = [0 for _ in range(n+1)]
        dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1,  1, 1, 1
        for num in range(6, n+1):
            if num % 2 == 0:
                dp[num] = dp[num // 2]
            elif num % 3 == 0:
                dp[num] = dp[num // 3]
            elif num % 5 == 0:
                dp[num] = dp[num // 5]
        return dp[-1]

sol = Solution()
n = 14
res = sol.isUgly(n)
print(res)

### another easy solution since it is an easy problem
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n in {1,2,3,4,5}:
            return True
        
        while n not in {1,2,3,4,5}:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                return False

        return True

sol = Solution()
n = 20
res = sol.isUgly(n)
print(res)
