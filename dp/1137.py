class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(None)
        def dp(n):
            if n == 0:
                return 0 
            elif n == 1:
                return 1
            elif n == 2:
                return 1
            else:
                return dp(n-1) + dp(n-2) + dp(n-3)
        return dp(n)
        