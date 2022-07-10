from functools import lru_cache
import re
from typing import List


# a naive approach
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dp(piles, cur):
            if len(piles) == 0:
                return cur
            elif len(piles) == 1:
                return cur + piles[0]
            else:
                a = min(dp(piles[2:], cur +piles[0]) , dp(piles[1: -1], cur + piles[0]))
                b =  min(dp(piles[1:-1], cur + piles[-1]), dp(piles[:-2], cur+ piles[-1]) )
                return max(a, b)
        res = dp(piles, 0)
        tsum = sum(piles)
        return True if res > tsum/ 2.0 else False

sol = Solution()
piles = [3, 7, 2]
res = sol.stoneGame(piles)
print(res)
 
# another approach with memorization
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return piles[i]
            elif j < i:
                return 0
            else:
                a = min(dp(i+2, j), dp(i+1, j-1)) + piles[i]
                b = min(dp(i+1, j-1), dp(i, j-2)) + piles[j]
                return max(a, b)
        res = dp(0, len(piles)-1)
        tsum = sum(piles)
        return True if res > tsum/ 2.0 else False

sol = Solution()
piles = [3, 7, 2]
res = sol.stoneGame(piles)
print(res)

# another more efficient approach
# actually 
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dp(i, j, player):
            if j < i:
                return 0
            elif j == i:
                return piles[i] if player == 0 else 0
            else:
                if player == 1:
                    return min(dp(i+1,j, 1-player), dp(i, j-1, 1-player))
                else:
                    return max(dp(i+1,j, 1- player) + piles[i], dp(i, j-1, 1-player) + piles[j])
        res = dp(0, len(piles)-1, 0)
        tsum = sum(piles)
        return True if res > tsum/ 2.0 else False

sol = Solution()
piles = [3, 7, 4, 2]
res = sol.stoneGame(piles)
print(res)

