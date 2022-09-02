from typing import List

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n, ans, tsum = len(beans), float('inf'), sum(beans)
        for i in range(n):
            res = tsum - beans[i] * (n - i)
            ans = min(ans, res)
        return ans
        
        