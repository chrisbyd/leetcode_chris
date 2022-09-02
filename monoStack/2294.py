from typing import List
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        start = 0
        for i, num in enumerate(nums):
            if num - nums[start]  > k:
                ans += 1
                start = i
        return ans
        