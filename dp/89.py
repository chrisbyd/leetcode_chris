from typing import List

#### easy dynamic programming problem
class Solution:
    def grayCode(self, n: int) -> List[int]:
        def dp(n):
            if n == 1:
                return [0,1]
            else:
                ans = dp(n-1) 
                new_ans = [2** (n-1) + i for i in ans[::-1]]
                return ans + new_ans
        return dp(n)
                

#### easy dynamic programming problem
## with cache
class Solution:
    def grayCode(self, n: int) -> List[int]:
        cache = {}
        def dp(n):
            if n not in cache:
                if n == 1:
                    ans =  [0,1]
                else:
                    ans = dp(n-1) 
                    new_ans = [2** (n-1) + i for i in ans[::-1]]
                    ans = ans + new_ans
                cache[n] =  ans
                return ans
            else:
                return cache[n]
        return dp(n)
                

#### with bottom up dynamic programmming
class Solution:
    def grayCode(self, n: int) -> List[int]:
        dp = {}
        dp[1] = [0 , 1]
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + [ 2 ** (i-1) + num for num in dp[i-1][::-1]]
        return dp[n]


