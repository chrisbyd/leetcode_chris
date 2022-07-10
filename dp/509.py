
### this is a super easy fibonacci algorithm
from functools import lru_cache


class Solution:
    def fib(self, n: int) -> int:
        @lru_cache(None)
        def recur(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return recur(n-1) + recur(n-2)
        return recur(n)
