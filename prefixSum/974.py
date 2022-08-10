from typing import List
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        presum = 0
        d = defaultdict(int)
        d[0] = 1
        ans = 0
        for num in nums:
            presum += num
            ans += d[presum % k]
            d[presum % k] += 1
        return ans
            
            
        