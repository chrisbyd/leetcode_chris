from typing import List
from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cumu = 0
        d = defaultdict(int)
        d[0] = 1
        ans = 0
        for num in nums:
            cumu += num
            if cumu - goal in d:
                ans += d[cumu- goal]
            d[cumu ] += 1
        return ans