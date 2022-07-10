from typing import List
# accepted  but only beats 5%
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        cumu = [0] * (n+1)
        csum = 0
        for i in range(n):
            csum += piles[i]
            cumu[i+1] = csum
        @lru_cache(maxsize=None)
        def dp(index, m, player):
            if index >= n:
                return 0
            elif index == n - 1 and player == 0:
                return piles[index]
            elif index == n - 1 and player == 1:
                return 0
            elif player == 0:
                ans = 0
                for i in range(1, 2* m +1):
                    max_index = index + i if index + i <= n else n 
                    ans = max(ans,cumu[max_index] -cumu[index] + dp(index+i, max(m,i), 1- player))
                return ans
            else:
                ans = float('inf')
                for i in range(1, 2* m +1):
                    max_index = index + i if index + i <= n else n 
                    ans = min(ans, dp(index+i, max(m,i), 1- player))
                return ans
        return dp(0, 1, 0)
                

sol = Solution()
piles = [2,7,9,4,4]
res = sol.stoneGameII(piles)
print(res)
                