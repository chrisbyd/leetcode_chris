from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        @lru_cache(None)
        def dp(i, j,  k):
            if k == 1:
                return max(cardPoints[i], cardPoints[j])
            else:
                a = cardPoints[i] + dp(i+1, j, k-1)
                b = cardPoints[j] + dp(i, j-1, k -1)
                return max(a, b )
        return dp(0, len(cardPoints)-1, k)


### this can actually turn it into another proble,

from typing import List
import sys
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        presum = [0]
        for point in cardPoints:
            presum.append(presum[-1] + point)
        left = n - k
        minimum =  sys.maxsize
        for j in range(left-1, n):
            i = j - left + 1
            tsum = presum[j+1] - presum[i]
            minimum = min(minimum, tsum)
        ans = presum[-1] - minimum
        return ans
            
        
        
        
        