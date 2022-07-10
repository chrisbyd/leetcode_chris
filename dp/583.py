from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        @lru_cache(None)
        def dp(index1, index2):
            if index1 == m:
                return 0
            elif index2 == n:
                return 0
            else:
                if word1[index1] == word2[index2]:
                    return 1 + dp(index1+1, index2 + 1)
                else:
                    return max(dp(index1 + 1, index2), dp(index1, index2 + 1))
        maxCom = dp(0, 0)
      
        return m + n - 2* maxCom
        
sol =  Solution()
word1 = "sea"
word2 = "eat"
res = sol.minDistance(word1, word2)
print(res)
