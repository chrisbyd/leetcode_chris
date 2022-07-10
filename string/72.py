

# bottom up dynamic programming
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[-1 for j in range(n + 1) ] for i in range(m + 1)]
        dp[-1][-1] = 0
        for i in range(m):
            dp[i][-1] = m - i
        for j in range(n):
            dp[-1][j] = n - j
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
        return dp[0][0]


                


word1 = "horse"
word2 = "ros"
sol = Solution()
res = sol.minDistance(word1, word2)
print(res)



#top down dynamic programming
# this is the solution

import collections
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = {}
        def dp(i, j):
            if i == m and j == n:
                return 0
            elif i == m and j < n:
                return n - j
            elif i < m and j ==n:
                return m -i
            else:
                if (i, j) not in memo:
                    if word1[i] == word2[j]:
                        memo[i, j] = dp(i+1, j+1)
                        return memo[i, j]
                    else:
                        memo[i, j] = min(dp(i+1, j+1), dp(i, j+1), dp(i+1, j)) + 1
                        return memo[i, j]
                else:
                    return memo[i,j]
        return dp(0, 0)

word1 = "horse"
word2 = "hrose"
sol = Solution()
res = sol.minDistance(word1, word2)
print(res)