from typing import List

class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [0 for i in range(n+1)]
        dp[1] = 0 
        for i in range(2, n+1):
            ans = 0
            for x in range(1, i):
                if i % x == 0 and dp[i-x] == 0:
       
                    ans = 1
                    dp[i] = ans

        return dp[-1]


sol = Solution()
n = 4
res = sol.divisorGame(n)
print(res)








        


        