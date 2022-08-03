
####at first sight, we could use dynamic programming
### but is there a better way?
class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(None)
        def dp(n):
            if n == 1:  return 0
            elif  n % 2 == 0:
                return 1 + dp(n // 2)
            else:
                return min(1 + dp(n+1), 1+ dp(n-1))
        return dp(n)
            
        
class Solution:
    def integerReplacement(self, n: int) -> int: