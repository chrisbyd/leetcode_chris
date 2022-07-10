from functools import lru_cache

# with lru cache
class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        memo[0] = 1
        memo[1] = 1
        ans = 0
        @lru_cache(None)
        def helper(n):
            if n in memo:
                return memo[n]
            else:
                ans = 0
                for i in range(n):
                    ans += helper(i) * helper(n-1-i)
                return ans
        return helper(n)



        
# with memory
class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def helper(n):
            if n in set([0,1]):
                return 1
            else:
                if n not in memo:
                    ans = 0
                    for i in range(n):
                        ans += helper(i) * helper(n-1-i)
                    memo[n] = ans
                    return ans
                else:
                    return memo[n]
        return helper(n)
