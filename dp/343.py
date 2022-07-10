
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n):
            ans = 0
            for j in range(1, i+1):
                ans = max(ans, j * dp[i - j])
            dp[i] = ans
        ans = 0
        for j in range(1, n):
            ans = max(ans, j* dp[n - j])
        
        return ans

sol = Solution()
n = 10
res = sol.integerBreak(n)
print(res)





        