##brutal force solution
from typing import List
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] == nums[i] + k or nums[j] == nums[i] - k:
                    ans += 1
        return ans


from collections import defaultdict
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cmap = defaultdict(int)
        ans = 0 
        for i in range(n-1, -1, -1):
            ans += cmap[nums[i] + k]
            ans += cmap[nums[i] - k]
            cmap[nums[i]] += 1
        return ans
        