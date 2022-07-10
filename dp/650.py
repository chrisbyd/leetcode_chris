
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        for i in range(2, n+1):
            tem = []
            for j in range(1, i):
                if i%j != 0:
                    tem.append(float("inf"))
                else:
                    tem.append(dp[j] + i //j )
            dp[i] = min(tem)
        return dp[-1]
                
sol = Solution()
n = 3
res = sol.minSteps(n)
print(res)



#  another solution with prime factorization
class Solution(object):
    def minSteps(self, n):
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans