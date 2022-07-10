

# time limit exceeds
# try to solve with out the second iteration
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (k + maxPts)
        for i in range(k, k+maxPts):
            if i <= n:
                dp[i] = 1
            else:
                dp[i] = 0
        for id in range(k-1, -1, -1):
            ans = 0
            for j in range(1, maxPts +1):
                ans += dp[id+j]
            dp[id] = 1/maxPts * ans 
        return dp[0]

sol = Solution()
n = 21
k = 17
maxPts = 10
res = sol.new21Game(n, k, maxPts)
print(res)
            


# this one gets accepted
# but still this solution is not concisea n
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (k + maxPts)
        for i in range(k, k+maxPts):
            if i <= n:
                dp[i] = 1
            else:
                dp[i] = 0
        ans = 0
        for j in range(k, k+ maxPts):
                ans += dp[j]
        dp[k-1] = ans / maxPts       
        end = k + maxPts -1
        for id in range(k-2, -1, -1):
            dp[id] = 1/maxPts * dp[id+1] + dp[id+1] - 1/maxPts *dp[end]
            end -= 1
        return dp[0] 

sol = Solution()
n = 21
k = 17
maxPts = 10
res = sol.new21Game(n, k, maxPts)
print(res)

# a solution offered by the discussion
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (k + maxPts)
        dp[k:n+1] = [1]* (n+1 - k)
        curr = min(maxPts, n-k+1)
        for i in range(k-1, -1, -1):
            dp[i] = curr / maxPts
            curr += dp[i] - dp[i+maxPts]
        return dp[0]
 